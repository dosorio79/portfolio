---
title: "CodeCollab — Collaborative Coding Interview Platform"
year: 2025
stack:
  - "React"
  - "Vite"
  - "Express"
  - "WebSockets"
  - "Pyodide"
context: "course"
course_name: "AI Dev Tools (DataTalksClub)"
course_role: "homework"
summary: "Real-time collaborative coding interview platform with in-browser execution."
repo: "https://github.com/dosorio79/ai-dev-tools-zoomcamp/tree/main/02-coding_platform"
video_url: "https://www.youtube.com/watch?v=huI30O4ScAw"
---

**Overview**
CodeCollab is a real-time interview-style coding platform inspired by CoderPad/CodeSignal, built to run entirely in-browser or in a single container.

**Core features**
- Live collaborative editor with presence and synchronized editing
- JavaScript sandbox execution in the browser
- Python execution via Pyodide (WASM)
- Shareable session links and stateless, ephemeral sessions

**Architecture notes**
- React + Vite frontend with WebSocket-driven sync
- Express backend for REST + WebSockets with in-memory session store
- One-origin deployment (frontend served by backend) to avoid CORS

**Local workflow**
- `npm run dev` runs frontend and backend concurrently
- Docker Compose for two-container dev
- Render deployment via single-container `Dockerfile.render`
