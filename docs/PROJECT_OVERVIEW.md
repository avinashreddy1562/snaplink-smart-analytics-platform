# SnapLink Project Overview

## Problem statement

Long URLs are difficult to share, remember, organize, and measure. SnapLink will provide locally runnable short-link creation, management, QR codes, and privacy-conscious analytics for an academic demonstration.

## Proposed solution and objectives

The system will let authenticated users create and manage short links, use a short URL or QR code, and inspect aggregated click analytics. Measurable objectives are: implement a protected REST API, persist normalized data in PostgreSQL, provide a React dashboard, implement a Django redirect fallback plus a locally testable Worker contract, and cover critical workflows with automated tests.

## Scope

Current Phase 0 scope is repository planning and tooling only. Subsequent phases cover authentication, links, redirects, analytics, QR codes, frontend, Worker, QA, and final documentation.

## Out of scope

Commercial billing, enterprise SSO, production geolocation, internet-scale load guarantees, managed hosting, and custom-domain DNS infrastructure are excluded from the academic prototype.
