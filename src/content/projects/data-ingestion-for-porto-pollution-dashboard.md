---
title: "Data Ingestion for Porto Pollution Dashboard"
year: 2024
stack:
  - "Python"
  - "Apache Airflow"
  - "PostgreSQL"
  - "MinIO"
  - "Docker"
context: "course"
course_name: "Big Data Analytics and Decision Making (ISEP)"
course_role: "capstone"
summary: "End-to-end ETL pipeline integrating urban mobility, air quality, and transit data for analytics-ready dashboards."
repo: "https://github.com/dosorio79/proFinal_BDDM_ISEP"
authors:
  - "Daniel Sampaio Osório"
  - "Diogo Dias Assunção Serra"
  - "Jorge Laginhas"
  - "Pedro Rodrigues"
  - "Tiago Fernandes"
---

2024 · Course — Big Data Analytics and Decision Making (ISEP)

End-to-end ETL pipeline integrating urban mobility, air quality, and transit data for analytics-ready dashboards.

**Purpose**
Create a reliable ingestion pipeline for multi-source urban data to support pollution analytics and dashboards.

**Approach**
Extracted data from Porto’s Urban Platform, GTFS feeds, and demographic sources, then orchestrated ELT into a star-schema warehouse with Airflow.

**Constraints**
Containerized the pipeline to keep the stack portable and reproducible across environments.

**Tech stack**
Python · Apache Airflow · PostgreSQL · MinIO · Docker

