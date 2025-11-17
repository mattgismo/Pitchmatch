# Pitchmatch🎤 **Pitch Match!** is a simple starter backend for a singing-performance app that analyzes pitch and timing.
This repo is a minimal, deployable prototype so you can get the service running and iterate quickly.

## What's included
- `main.py` — FastAPI app with a colorful landing page and a simple JSON API route.
- `requirements.txt` — Python dependencies.
- `Dockerfile` — Build instructions for the Docker image.
- `docker-compose.yml` — Local development helper.
- `.github/workflows/ci.yml` — CI workflow that builds, tests, and pushes the Docker image to Docker Hub.

## Quickstart (local)
1. Install Docker and Docker Compose.
2. Build and run locally:
   ```bash
   docker-compose up --build
