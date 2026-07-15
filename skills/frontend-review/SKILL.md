---
name: frontend-review
description: Review frontend changes for behavioral correctness, regressions, accessibility, responsive layout, performance, security, and test coverage. Use when a user asks for a frontend code review, UI pull-request review, regression analysis, or prioritized findings without requesting implementation.
---

# Frontend Review

## Workflow

1. Read the change description, diff, affected components, routes, data clients, styles, and tests.
2. Trace each changed interaction from user input through state and network behavior to rendered output.
3. Check correctness across loading, empty, error, success, validation, cancellation, and repeated-interaction paths where applicable.
4. Check semantic structure, keyboard access, focus behavior, labels, announcements, contrast assumptions, and responsive layout.
5. Check avoidable rendering work, oversized client bundles, unsafe HTML, exposed secrets, and trust-boundary mistakes.
6. Confirm tests cover the risky behavior rather than only snapshots or implementation details.
7. Report only evidence-backed findings, ordered by severity, with file and line references and a concrete fix.

## Output contract

- Lead with blocking findings, then non-blocking findings.
- For every finding include impact, evidence, affected path, and a minimal remediation.
- If no issue is found, state that explicitly and list residual unverified risks.

## Guardrails

- Do not edit files unless the user separately asks for fixes.
- Do not report taste, formatting, or framework preference as a defect.
- Do not infer runtime behavior from filenames or a diff alone when the implementation is available.
- Do not claim browser behavior was verified unless it was exercised.

## Failure handling

If the diff, affected implementation, or acceptance criteria are missing, identify the missing evidence and limit the review to what can actually be established.
