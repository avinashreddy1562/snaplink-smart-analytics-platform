# Security

## Phase 1 controls

- `DJANGO_SECRET_KEY` is required from the environment or `.env`; no application secret is committed.
- Django's password hashing and password validators are enabled.
- The custom user model is configured before the initial migration.
- CORS uses an explicit local frontend origin rather than allowing every origin.
- Django's CSRF, clickjacking, authentication, and security middleware remain enabled.
- The health endpoint exposes only application/database status, never credentials or connection details.

JWT endpoint behavior, token revocation, rate limits, URL validation, authorization policy, and analytics privacy retention are deferred to later phases and will be documented when implemented.
