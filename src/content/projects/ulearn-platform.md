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

Micro-learning platform that generates 15-minute lessons with a multi-agent backend and a calm, fast frontend.

**Purpose**
Deliver tightly scoped lessons that avoid open-ended chat drift and produce reusable structured outputs.

**Approach**
Designed a multi-agent pipeline that plans, generates structured blocks, and validates format/time budget, with deterministic checks and LLMs only for content generation.

**Constraints**
Kept the user flow stateless with append-only telemetry and support for MongoDB or in-memory backends.

**Recent updates**
Added snapshots, an architecture diagram, and a demo video for quick context.

**Tech stack**
React · FastAPI · MongoDB · Pyodide

