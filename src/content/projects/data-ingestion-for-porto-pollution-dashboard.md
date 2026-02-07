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

Built a full data pipeline that extracts multi-source urban data from Porto’s Urban Platform, GTFS feeds, and demographic sources.
Automated ingestion, transformation, and loading into a star-schema warehouse with Airflow orchestration.
Containerized the stack with Docker, using MinIO as the data lake and PostgreSQL as the warehouse.
