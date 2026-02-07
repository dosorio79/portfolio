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

2025 · Course — AI Dev Tools (DataTalksClub)

MCP server that indexes GitHub docs and exposes search, read, and scrape tools.

**Purpose**
Provide a small, focused MCP server for documentation lookup with simple, reusable tools.

**Approach**
Downloaded repo ZIPs, indexed Markdown with `minsearch`, and exposed `scrape`, `search_repo_index`, and `read_repo_file` tools via FastMCP with config-driven repos.

**Constraints**
Kept the server lightweight, config-first, and suitable for STDIO-based MCP workflows.

**Tech stack**
Python · FastMCP · uv · minsearch

