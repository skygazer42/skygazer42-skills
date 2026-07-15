---
name: backend-debugging
description: Diagnose backend failures by reproducing symptoms, tracing requests and data, testing hypotheses, and identifying the root cause and blast radius. Use when a user reports an API error, failed job, database anomaly, timeout, integration failure, intermittent backend bug, or production-like incident and wants diagnosis.
---

# Backend Debugging

## Workflow

1. Establish the exact symptom, expected behavior, environment, timing, request or job identity, and available evidence.
2. Locate the real entrypoint and trace the path through callers, configuration, queues, storage, caches, and external services.
3. Reproduce the failure with the smallest safe command, request, or test. Preserve the exact output.
4. Inspect relevant logs, metrics, recent changes, configuration differences, and data shape without exposing secrets.
5. Form a short ranked hypothesis list. Run the cheapest discriminating check for each hypothesis instead of making speculative edits.
6. Identify the root cause, triggering condition, affected sibling paths, and why existing defenses or tests missed it.
7. Recommend the smallest fix and verification. Implement only when the user also asks for a fix.

## Output contract

- State the diagnosed root cause and confidence level.
- Provide reproduction or decisive evidence, affected paths, and blast radius.
- Separate confirmed facts, supported inference, and remaining unknowns.
- Give a minimal fix and verification plan without claiming an unperformed recovery.

## Guardrails

- Do not change code merely to test a guess when a read-only check can distinguish it.
- Do not treat symptom suppression, retries, or restarts as the root cause.
- Do not query or mutate production data beyond the user's explicit authorization.
- Do not print credentials, tokens, personal data, or full sensitive payloads.

## Failure handling

If the failure cannot be reproduced, preserve the strongest evidence, narrow the conditions, and identify the next observation needed. Do not invent logs, runtime state, or a definitive cause.
