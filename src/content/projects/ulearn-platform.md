---
title: "uLearn — Agentic Micro-Learning Platform"
year: 2026
stack:
  - "React"
  - "FastAPI"
  - "MongoDB"
  - "Pyodide"
context: "course"
course_name: "AI Dev Tools (DataTalksClub)"
course_role: "capstone"
summary: "Micro-learning platform that generates 15-minute lessons with a multi-agent backend and a calm, fast frontend."
repo: "https://github.com/dosorio79/ulearn-platform"
snapshot: "/images/snapshot_ulearn.png"
architecture_diagram: "/images/architecture_ulearn.png"
video_url: "https://youtu.be/HlbSlIufW2k"
---

**Overview**
uLearn delivers 15-minute, tightly scoped lessons to avoid open-ended “chat drift,” producing structured outputs that can be reused as Markdown or Jupyter notebooks.

**Backend workflow**
- Multi-agent pipeline: plan → generate structured blocks → validate format/time budget
- Deterministic planning/validation; only content generation uses an LLM
- MCP tools run advisory checks (e.g., Python syntax hints) and log to telemetry

**Frontend UX**
- Structured block rendering with per-section copy
- Full-lesson exports and in-browser Python execution via Pyodide

**Telemetry and persistence**
- Stateless user experience; append-only telemetry for requests, summaries, attempts, failures
- MongoDB or in-memory backends to support local dev and demo mode without external dependencies
