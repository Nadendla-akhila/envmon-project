# Environmental Monitoring & Pollution Control

Lightweight full-stack prototype for collecting sensor data, visualizing it, and raising alerts when pollution thresholds are exceeded.

## Features
- REST API (FastAPI) to ingest sensor telemetry and serve historical data
- PostgreSQL for storage (with PostGIS-ready column if desired)
- Simple React frontend to show real-time charts and list alerts
- Dockerized components and docker-compose for local dev

## Quick start
1. Copy files into a project folder.
2. Create `.env` from `.env.example` and update secrets.
3. `docker-compose up --build`
4. Backend: http://localhost:8000/docs
5. Frontend: http://localhost:3000
