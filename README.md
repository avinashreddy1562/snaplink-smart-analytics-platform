# SnapLink – Smart Link Generation and Analytics Platform

SnapLink is a final-year Bachelor’s project for creating, managing, and measuring short links. It will be a locally runnable React, Django REST Framework, PostgreSQL, and Cloudflare Worker application.

## Current status

**Phase 1 complete: Django foundation.** The backend now has environment-based PostgreSQL configuration, a custom user model, an initial migration, and `/api/health/`. Frontend, links, authentication endpoints, redirects, analytics, and the Worker remain deferred to their planned phases.

## Target stack

- React, Vite, TypeScript
- Python, Django, Django REST Framework
- PostgreSQL
- Cloudflare Workers / Wrangler
- pytest, Vitest, React Testing Library, Playwright (where practical)

## Repository layout

```text
backend/       Django foundation and tests (Phase 1 onward)
frontend/      React application (Phase 7 onward)
worker/        Cloudflare redirect Worker (Phase 8 onward)
docs/          Architecture, requirements, review, and project documentation
.github/       Continuous-integration workflows
```

## Local prerequisites

Planned local execution requires Python, Node.js, PostgreSQL (or Docker Compose), and Wrangler for the Worker. See [the architecture decisions](docs/ARCHITECTURE.md) and [review](docs/REVIEW.md) for current constraints.

For the backend setup, migrations, server, and tests, see [Local Setup](docs/LOCAL_SETUP.md).

## Documentation

- [Project overview](docs/PROJECT_OVERVIEW.md)
- [Requirements traceability](docs/REQUIREMENTS.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Specification review](docs/REVIEW.md)
- [Open-source references](docs/OPEN_SOURCE_REFERENCES.md)

## License

This repository is licensed under the [MIT License](LICENSE).
