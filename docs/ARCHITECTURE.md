# Architecture

## Target architecture

SnapLink is a locally runnable, five-layer academic application: React provides the presentation layer; Django REST Framework owns API and business rules; PostgreSQL persists accounts, links, and events; a Cloudflare Worker implements the deployable redirect contract; and Django remains the reliable local redirect fallback.

The authoritative visual source is [system-architecture.mmd](diagrams/system-architecture.mmd). The Worker and fallback must return equivalent public link states (valid, missing, disabled, expired) once implemented.

## Phase 0 decisions

| Decision | Reasoning |
| --- | --- |
| TypeScript for frontend and Worker | It is preferred in the specification and improves API/UI safety. |
| PostgreSQL remains the application database | SQLite is not selected as a development substitute. |
| Django owns the custom user model in Phase 1 | Defining it before the first migration avoids a risky replacement. |
| Docker Compose is optional | It provides a consistent PostgreSQL path without making Docker a prerequisite. |
| No application code in Phase 0 | The requested scope is repository and planning only. |
| Django 5.2 LTS for Phase 1 | It supports the installed Python 3.14 runtime and provides a stable project baseline. |
| SQLite only for automated tests | PostgreSQL is the runtime database; the test-only setting keeps automated checks reproducible without a local service. |

## Specification conflict resolved

Section 55 says to create the base structure and then implement Phase 1 on first receipt, whereas Section 50 separates Phase 0 and this request explicitly says “Start with Phase 0 only.” The narrower instruction governs: this repository ends at Phase 0 with no Django project, database schema, or executable frontend.

## Deferred contracts

Phase 1 must define environment loading, PostgreSQL settings, a health endpoint, migrations, and the custom user model. Before Phase 4 and Phase 8, a shared redirect lookup response and status-code contract must be written so Django and the Worker cannot drift.
