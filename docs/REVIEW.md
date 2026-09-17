# Governing Specification Review

## Concrete gaps, ambiguities, contradictions, and risks

| Finding | Impact | Resolution / owner |
| --- | --- | --- |
| Phase 50 isolates Phase 0, but Section 55 directs initial work through Phase 1. | Scope conflict. | This work ends after Phase 0; decision recorded in Architecture. |
| “Logout” is required with JWT but token storage, refresh rotation, and blacklist policy are unspecified. | A nominal logout could be ineffective. | Phase 2 must choose a documented refresh-token revocation/rotation strategy and storage model. |
| The Worker is told to look up a destination through a backend API, but no endpoint, authentication, cache, or failure policy is defined. | Redirect parity and security can drift. | Define a dedicated public lookup contract before Phase 4/8. |
| “Appropriate status codes” for expired and disabled links are not specified. | Browser/API/Worker behavior may diverge. | Document an explicit state-to-response matrix before redirect implementation. |
| “Approximate unique visitors” omits time-window duration, secret rotation, and retention/deletion rules. | Privacy and reported totals are inconsistent. | Phase 5 must choose documented values and test deterministic behavior. |
| Country collection does not define the request input or presentation label for simulation. | Simulated data could be mistaken for real data. | Create a provider interface and visibly label demo-simulated geography. |
| Link lifecycle diagram appears sequential although active, disabled, expired, and deleted states can overlap. | Restore/reactivation rules are ambiguous. | Define a state machine and precedence before Phase 3. |
| CI must eventually test all apps, while Phase 0 has no app source or dependency lockfiles. | An apparently complete CI would fail or be misleading. | Add an honest structure-only CI job now; expand it only when runnable applications exist. |
| Dependency versions are prescribed only as product names. | Unpinned `latest` packages are not reproducible. | Resolve and commit lockfiles when each runnable package is introduced. |
| Python 3.14 is installed locally, but target dependency compatibility is not established. | Installation may fail in Phase 1. | Choose and document a supported Python version during Django setup; CI should use it. |
| “No raw IP dashboard display” does not define collection, hashing salt, access, or retention. | Privacy handling could be under-specified. | Add a data-retention policy before analytics event collection. |

## Phase 0 implementation risks

PostgreSQL, Docker, and Wrangler are not installed in the inspected environment. Docker Compose remains a setup option, but database and Worker execution cannot be verified in Phase 0. Frontend/Worker manifests intentionally have no lockfiles until their applications are created, so dependency installation is deferred.
