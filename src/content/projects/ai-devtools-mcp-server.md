---
title: "AI Dev Tools Zoomcamp — MCP Server"
year: 2025
stack:
  - "Python"
  - "FastMCP"
  - "uv"
  - "minsearch"
context: "course"
course_name: "AI Dev Tools (DataTalksClub)"
course_role: "homework"
summary: "MCP server that indexes GitHub docs and exposes search, read, and scrape tools."
repo: "https://github.com/dosorio79/ai-dev-tools-zoomcamp/tree/main/03-mcp"
video_url: "https://youtu.be/RSdp_J6mOFA"
---

**Overview**
MCP server that downloads documentation repositories, builds a lightweight search index, and exposes tools to search and read docs. Includes a simple web scraping tool backed by Jina Reader.

**Core capabilities**
- Download GitHub repo ZIPs and cache them locally
- Index Markdown docs with `minsearch`
- Expose MCP tools: `scrape`, `search_repo_index`, `read_repo_file`

**Architecture notes**
- FastMCP server entrypoint in `main.py`
- Config-driven repos and indexing via `server_config.yaml`
- Search and ZIP parsing helpers in `search.py`
- Jina Reader fetch helper in `scrape.py`

**Local workflow**
- `uv sync` for a dev install (exposes `hw3-mcp`)
- `uv run hw3-mcp` to build the index and serve MCP tools over STDIO
- Optional MCP Inspector for interactive testing
