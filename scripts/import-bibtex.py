#!/usr/bin/env python3
"""
Import publications from a BibTeX file into this repository.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
from dataclasses import dataclass
import sys
import unicodedata

from bibtexparser.bparser import BibTexParser
from slugify import slugify
from pylatexenc.latex2text import LatexNodes2Text


latex_converter = LatexNodes2Text()
OUTPUT_DIR = Path("src/content/publications")


# ---------------------------------------------------------
# Model
# ---------------------------------------------------------

@dataclass(frozen=True, slots=True)
class Publication:
    title: str
    year: int
    journal: str
    authors: list[str]
    doi: str | None
    link: str | None
    type: str
    featured: bool
    summary: str
    first_author: bool


# ---------------------------------------------------------
# Ingestion
# ---------------------------------------------------------

def read_bibtex_file(file_path: str) -> list[dict]:
    parser = BibTexParser(common_strings=True)

    with open(file_path, "r", encoding="utf-8") as bibtex_file:
        try:
            bib_database = parser.parse_file(bibtex_file)
        except AttributeError:
            import bibtexparser
            bib_database = bibtexparser.load(bibtex_file, parser=parser)

    return bib_database.entries


# ---------------------------------------------------------
# Cleaning
# ---------------------------------------------------------

def _clean_text(value: str) -> str:
    if not value:
        return ""

    value = latex_converter.latex_to_text(value)
    value = re.sub(r"[{}]", "", value)
    value = unicodedata.normalize("NFC", value)

    # collapse whitespace globally
    value = " ".join(value.split())

    return value.strip()


# ---------------------------------------------------------
# Filtering
# ---------------------------------------------------------

def filter_entries(entries: list[dict]) -> list[dict]:
    return [e for e in entries if e.get("ENTRYTYPE") == "article"]


# ---------------------------------------------------------
# Helpers
# ---------------------------------------------------------

def _infer_publication_type(journal: str) -> str:
    journal = journal.lower()

    preprint_tokens = (
        "biorxiv",
        "medrxiv",
        "arxiv",
        "openrxiv",
    )

    return "preprint" if any(t in journal for t in preprint_tokens) else "peer-reviewed"


def _resolve_identifiers(entry: dict) -> tuple[str | None, str | None]:
    doi = entry.get("doi")
    url = entry.get("url")

    if doi:
        doi = doi.strip()
        return doi, f"https://doi.org/{doi}"

    if url:
        return None, _clean_text(url)

    return None, None


def _extract_summary(entry: dict) -> str:
    raw = entry.get("abstract") or entry.get("note") or ""
    return _clean_text(raw)


# ---------------------------------------------------------
# Normalization
# ---------------------------------------------------------

def normalize_entry(entry: dict) -> Publication:

    title = _clean_text(entry.get("title", ""))
    if not title:
        raise ValueError("Missing title")

    year_raw = entry.get("year")
    if not year_raw or not year_raw.isdigit():
        raise ValueError("Invalid year")

    year = int(year_raw)

    journal = _clean_text(entry.get("journal", ""))

    authors_raw = entry.get("author", "")
    authors = [
        _clean_text(a)
        for a in authors_raw.split(" and ")
        if a.strip() and a.lower() not in {"others", "et al."}
    ]

    if not authors:
        raise ValueError("Missing authors")

    doi, link = _resolve_identifiers(entry)

    pub_type = _infer_publication_type(journal)
    summary = _extract_summary(entry)

    first_author = "osório" in authors[0].lower() or "osorio" in authors[0].lower()

    return Publication(
        title=title,
        year=year,
        journal=journal,
        authors=authors,
        doi=doi,
        link=link,
        type=pub_type,
        featured=False,
        summary=summary,
        first_author=first_author,
    )


# ---------------------------------------------------------
# Pipeline Safety
# ---------------------------------------------------------

def deduplicate(publications: list[Publication]) -> list[Publication]:

    seen = set()
    unique = []

    for pub in publications:
        key = pub.doi or pub.title.lower()

        if key in seen:
            continue

        seen.add(key)
        unique.append(pub)

    print(f"Deduplicated to {len(unique)} publications.")
    return unique


def sort_publications(publications: list[Publication]) -> list[Publication]:

    return sorted(
        publications,
        key=lambda p: (
            p.type != "peer-reviewed",
            -p.year,
        )
    )


# ---------------------------------------------------------
# Export
# ---------------------------------------------------------

def _build_slug(title: str) -> str:
    return slugify(title, max_length=60)


def _yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f"\"{escaped}\""


def _format_publication_md(pub: Publication) -> str:

    lines = [
        "---",
        f"title: {_yaml_quote(pub.title)}",
        f"year: {pub.year}",
        f"journal: {_yaml_quote(pub.journal)}",
        "authors:",
        *[f"  - {_yaml_quote(a)}" for a in pub.authors],
    ]

    if pub.link:
        lines.append(f"link: {_yaml_quote(pub.link)}")

    lines.extend([
        f"type: {_yaml_quote(pub.type)}",
        f"featured: {str(pub.featured).lower()}",
        f"first_author: {str(pub.first_author).lower()}",
        "---",
        "",
        pub.summary,
        "",
    ])

    return "\n".join(lines)


def _clean_output_directory(output_dir: Path) -> None:

    if not output_dir.exists():
        return

    for file in output_dir.glob("*.md"):
        file.unlink()

    print("Cleaned stale publication files.")


def export_publications(publications: list[Publication], output_dir: Path) -> None:

    output_dir.mkdir(parents=True, exist_ok=True)
    _clean_output_directory(output_dir)

    seen_slugs = set()

    for pub in publications:

        slug = _build_slug(pub.title)

        if slug in seen_slugs:
            raise ValueError(f"Duplicate slug detected: {slug}")

        seen_slugs.add(slug)

        file_path = output_dir / f"{slug}.md"
        file_path.write_text(_format_publication_md(pub), encoding="utf-8")

    print(f"Exported {len(publications)} publications.")


# ---------------------------------------------------------
# CLI
# ---------------------------------------------------------

def parse_args() -> argparse.Namespace:

    parser = argparse.ArgumentParser(
        description="Import a BibTeX file into Markdown publications."
    )

    parser.add_argument("bibtex_path")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=OUTPUT_DIR,
    )

    return parser.parse_args()


# ---------------------------------------------------------
# Runner
# ---------------------------------------------------------

def main() -> None:

    args = parse_args()

    print("Step 1/6: reading BibTeX file...")
    entries = read_bibtex_file(args.bibtex_path)
    print(f"Loaded {len(entries)} raw entries.")

    print("Step 2/6: filtering article entries...")
    entries = filter_entries(entries)

    print("Step 3/6: normalizing entries...")
    publications = []
    errors = []

    for entry in entries:
        try:
            publications.append(normalize_entry(entry))
        except ValueError as exc:
            errors.append(str(exc))

    if errors:
        print("Skipped entries:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)

    if not publications:
        raise RuntimeError("Pipeline produced zero publications.")

    print("Step 4/6: deduplicating...")
    publications = deduplicate(publications)

    print("Step 5/6: sorting...")
    publications = sort_publications(publications)

    print("Step 6/6: exporting Markdown...")
    export_publications(publications, args.output_dir)

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()
