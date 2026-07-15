---
name: backend-implementation
description: Implement or modify production backend APIs, services, jobs, data access, schemas, and integrations. Use when a user asks to add server behavior, change an endpoint, persist data, introduce a migration, connect an external service, or write backend tests.
---

# Backend Implementation

## Workflow

1. Read the request, acceptance criteria, entrypoint, callers, contracts, models, migrations, configuration, and existing tests.
2. Trace the request and data path end to end. Reuse existing service boundaries, helpers, error types, and installed dependencies.
3. Define trust boundaries before editing: validate untrusted input, enforce authentication and authorization, and avoid exposing secrets or internal errors.
4. Implement the smallest coherent change. Preserve compatibility unless a breaking change is explicitly accepted.
5. Protect data with appropriate constraints, transactions, idempotency, concurrency handling, timeouts, and bounded retries where the real path requires them.
6. Add or update the smallest tests that cover success, important failure paths, and the regression risk.
7. Run focused tests and relevant type, lint, migration, and integration checks. Report files changed, behavior, checks, and remaining deployment concerns.

## Output contract

- Deliver repository changes that follow the existing architecture.
- State contract, schema, configuration, or migration changes explicitly.
- Separate locally verified behavior from deployment-dependent behavior.

## Guardrails

- Do not add a dependency or abstraction when existing code or the standard library suffices.
- Do not weaken validation, authorization, data constraints, or error handling to shorten the change.
- Do not embed credentials, log sensitive values, or silently swallow failures.
- Do not run destructive migrations or production writes without explicit authorization and a recovery plan.

## Failure handling

If an external service, database, credential, or deployment environment is unavailable, keep the implementation scoped to verified contracts, preserve the failing evidence, and state the exact integration check that remains.
