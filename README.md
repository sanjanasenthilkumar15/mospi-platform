# StatIQ — Data Ingestion & Database Stack

## What your project does
StatIQ is a comprehensive AI-powered Data Ingestion and Database platform. It provides an end-to-end data pipeline orchestration, object storage, and an interactive database layer combined with an AI engine to enable natural language to SQL queries. 

## Problem statement & solution
**Problem**: Managing complex data ingestion, storage, and making data accessible to non-technical users is challenging and requires extensive engineering effort.
**Solution**: StatIQ integrates PostgreSQL (with TimescaleDB), MinIO (object storage), Redis (caching), Apache Airflow (orchestration), and Ollama (AI layer) into a unified platform. It simplifies data ingestion and provides a backend API and frontend interface for users to easily interact with and visualize their data, including using AI to query the database using natural language.

## Features
* **Robust Data Storage**: PostgreSQL 16 with TimescaleDB for time-series data handling.
* **Data Pipeline Orchestration**: Apache Airflow for scheduling and managing data workflows.
* **Object Storage**: S3-compatible MinIO for raw, parquet, and processed data.
* **AI Engine**: Integrated Ollama engine for Natural Language to SQL (NL-SQL) capabilities.
* **Caching & Rate Limiting**: Redis 7 for high-performance data caching.
* **Interactive Frontend**: React + Vite frontend for user interactions.

## Technologies used
* **Backend**: Python, FastAPI, PostgreSQL, TimescaleDB, Redis, MinIO
* **Frontend**: React, Vite, Nginx
* **AI/ML**: Ollama
* **Orchestration**: Apache Airflow, Docker, Docker Compose

## Steps to install and run
1. Clone the repository to your local machine.
2. Ensure you have Docker and Docker Compose installed.
3. Open a terminal in the root directory of the project.
4. Build and start the services using Docker Compose:
   ```bash
   docker-compose up -d --build
   ```
5. Access the services:
   * **Frontend**: http://localhost:3000
   * **Backend API**: http://localhost:8000
   * **pgAdmin**: http://localhost:5050
   * **MinIO Console**: http://localhost:9001
   * **Airflow Web UI**: http://localhost:8080

## Any required environment variables
Create a `.env` file based on `.env.example` or rely on the defaults provided in `docker-compose.yml`. Key variables include:
* `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`
* `JWT_SECRET`
* `OLLAMA_HOST`
* `MINIO_ROOT_USER`, `MINIO_ROOT_PASSWORD`

## Screenshots or sample inputs
*(Add screenshots of the Airflow DAGs, Frontend Dashboard, or sample NL-SQL inputs here once running)*
