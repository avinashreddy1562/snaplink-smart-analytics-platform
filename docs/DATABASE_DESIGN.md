# Database Design

## Phase 1 schema

The initial migration creates the project-owned `accounts_user` table before any other application migration. It extends Django's `AbstractUser` with a unique email address and `created_at`/`updated_at` timestamps. Django supplies the secure password-hash field, active/staff flags, groups, permissions, and authentication metadata.

Using a custom user model from the first migration prevents the unsafe migration path of replacing Django's default user model later. Link and analytics tables are deliberately deferred to their respective phases.

## Runtime database

PostgreSQL is the required application database. The `docker-compose.yml` service provides PostgreSQL 16 for local use. SQLite is configured only in `config.settings_test` to keep automated tests independent from an unavailable local PostgreSQL service.
