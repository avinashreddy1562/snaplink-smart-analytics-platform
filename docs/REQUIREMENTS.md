# Requirements Traceability

## Functional requirements

| ID | Requirement | Planned phase |
| --- | --- | --- |
| FR-001 | Users can register, authenticate, refresh tokens, and manage their profile. | 2 |
| FR-002 | Authenticated users can create, view, update, soft-delete, and restore their own links. | 3 |
| FR-003 | Links support secure automatic slugs, validated custom aliases, state, and expiration. | 3–4 |
| FR-004 | A valid short URL records an event and redirects; missing, disabled, and expired links are distinguished. | 4–5 |
| FR-005 | Owners can view privacy-conscious aggregate analytics and recent events without raw IP exposure. | 5 |
| FR-006 | Active links have deterministic, locally generated QR codes. | 6 |
| FR-007 | The React application exposes public and protected user flows. | 7 |
| FR-008 | The Worker implements the documented redirect contract while Django remains a local fallback. | 8 |

## Non-functional requirements

| ID | Requirement |
| --- | --- |
| NFR-001 | Core functionality runs locally using PostgreSQL and no paid service. |
| NFR-002 | Secrets are environment-based and never committed. |
| NFR-003 | Authorization restricts private links and analytics to their owner. |
| NFR-004 | APIs validate input and use structured, readable errors. |
| NFR-005 | Critical functionality is automated-tested and documented. |
| NFR-006 | Analytics are privacy-conscious and candid about approximation/simulation. |

## Phase boundary

Only documentation, manifests, directory layout, environment examples, and CI structure are implemented in Phase 0. None of the functional requirements above is claimed implemented yet.
