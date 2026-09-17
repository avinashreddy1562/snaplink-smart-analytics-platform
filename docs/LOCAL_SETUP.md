# Local Setup

## Phase 1 backend

Prerequisites: Python 3.14, PostgreSQL 16 or Docker Compose, and Node.js for later phases.

1. Copy `.env.example` to `.env` and replace `DJANGO_SECRET_KEY` and the database password.
2. Start PostgreSQL with `docker compose up -d postgres`, or create a local PostgreSQL database matching `.env`.
3. Create a virtual environment: `python -m venv .venv`.
4. Install the exact verified backend set: `.\\.venv\\Scripts\\python -m pip install -r backend\\requirements.lock`. The broader `requirements.txt` remains the maintained dependency declaration.
5. Apply migrations: from `backend`, run `..\\.venv\\Scripts\\python manage.py migrate`.
6. Start the API: `..\\.venv\\Scripts\\python manage.py runserver`.

The health endpoint is available at `http://127.0.0.1:8000/api/health/` after PostgreSQL is reachable.

## Automated tests

From `backend`, run `..\\.venv\\Scripts\\python -m pytest -q`. Tests deliberately use the SQLite-only `config.settings_test` module; production and normal local runtime continue to use PostgreSQL.
