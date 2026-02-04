---
title: "GitHub Q&A Agent"
year: 2025
stack:
  - "Python"
  - "Streamlit"
  - "OpenAI API"
  - "Pydantic AI"
  - "ChromaDB"
context: "course"
course_name: "AI Agents Crashcourse (DataTalksClub)"
repo: "https://github.com/dosorio79/ai-agent-crashcourse"
snapshot: "/images/snapshot_githubrepoQA.png"
architecture_diagram: "/images/snapshotgithubrepoQA_cli.png"
---

**Overview**
Streamlit app + CLI pipeline for asking questions about GitHub repo docs with an AI-powered agent.

**Core features**
- Ingest and chunk Markdown docs (simple, sliding, paragraph, section)
- Text, vector, and hybrid search over chunks
- Conversational agent using OpenAI with Pydantic AI
- Streamlit UI for interactive Q&A and a CLI for terminal workflows

**Goal**
Demonstrate a modular AI pipeline that moves from notebook experimentation to a usable interface.
