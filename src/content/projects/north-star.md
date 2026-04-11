---
title: "North Star"
year: 2026
stack:
  - "React 18"
  - "TypeScript"
  - "Vite"
  - "Tailwind CSS v4"
  - "FastAPI"
  - "Python 3.13"
  - "scikit-learn"
  - "pandas"
context: "independent"
summary: "Conference schedule planning app for Data Makers Fest 2026 that turns broad interests into a workable agenda using recommendation scoring, conflict checks, and calendar export."
tags:
  - "Hackathon"
  - "Private repo"
  - "Shared project"
---

North Star is a conference schedule planning app for Data Makers Fest 2026. It helps attendees turn broad interests into a workable event agenda by combining session metadata, recommendation scoring, conflict checks, and calendar export.

Built during the DSPT Vibe Coding Hackathon dedicated to Data Makers Fest, this is an independent project by the repository authors. It is not an official Data Makers Fest application and is not maintained, sponsored, endorsed, or operated by the event organization.

**Scope**
Support planning for Data Makers Fest 2026, held from May 4 to May 6, 2026 at Alfandega do Porto, Portugal.

**What it does**
Loads conference sessions from the event workbook, lets attendees filter by track, talk type, level, topic, and speaker, ranks sessions with a TF-IDF recommendation model, detects schedule conflicts before agenda changes are saved, stores the attendee profile and agenda locally in the browser, and exports the saved agenda as Markdown or `.ics`.

**Architecture**
The repository is split into three parts: `frontend/` for the React client, `backend/` for the FastAPI API and recommendation logic, and `data/` for the Excel workbook used as the source of conference schedule data.

**Tech stack**
React 18 · TypeScript · Vite · Tailwind CSS v4 · Vitest · Testing Library · FastAPI · Python 3.13 · pandas · openpyxl · scikit-learn · pytest · httpx · uv · npm · make · GitHub Actions
