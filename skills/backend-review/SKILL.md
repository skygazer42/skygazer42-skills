---
name: backend-review
description: Review backend changes for correctness, authorization, security, data integrity, concurrency, reliability, compatibility, observability, and test coverage. Use when a user asks for an API, service, database, migration, job, or backend pull-request review without asking for implementation.
---

# Backend Review

## Workflow

1. Read the change description, diff, affected entrypoints, callers, contracts, models, migrations, configuration, and tests.
2. Trace changed request and data paths through validation, authorization, business logic, persistence, external calls, and response handling.
3. Check success and failure behavior, including partial failure, rollback, duplicate delivery, retries, timeouts, cancellation, and concurrent execution where applicable.
4. Check trust boundaries, injection risks, access control, secret handling, sensitive logging, and information disclosure.
5. Check schema compatibility, constraints, transactions, migration safety, resource cleanup, observability, and operational impact.
6. Confirm tests cover the highest-risk behavior and fail for the regression they claim to prevent.
7. Report evidence-backed findings in severity order with file and line references, impact, affected path, and a minimal remediation.

## Output contract

- Separate blocking and non-blocking findings.
- Do not bury correctness or security defects under general summaries.
- If no defect is found, state that and list remaining unverified integration or deployment risks.

## Guardrails

- Do not edit files unless the user separately asks for fixes.
- Do not call formatting, naming, or architecture preference a correctness defect without concrete impact.
- Do not infer database or runtime behavior when the implementation, migration, or configuration can be read.
- Do not expose secrets found during review; identify their location safely.

## Failure handling

If required code, schema, deployment constraints, or test output is missing, list the missing evidence and limit conclusions to the paths that can be verified.
