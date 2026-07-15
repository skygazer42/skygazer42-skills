---
name: frontend-testing
description: Verify frontend behavior with the repository's existing test tools and, when available, a real browser. Use when a user asks to test a UI flow, reproduce a frontend bug, add focused frontend coverage, inspect console or network failures, or verify responsive and keyboard behavior.
---

# Frontend Testing

## Workflow

1. Identify the acceptance criteria, supported browsers and viewports, start command, test command, and relevant existing tests.
2. Prefer the repository's installed test runner and browser tooling. Start the real application when the behavior depends on integration.
3. Exercise the primary path plus the smallest meaningful set of loading, error, empty, validation, repeat-action, and navigation paths.
4. Check keyboard operation, focus movement, accessible names, visible feedback, responsive breakpoints, console errors, and failed requests as applicable.
5. When asked to add coverage, write the smallest behavior-focused test that fails for the regression and passes for the intended behavior.
6. Record the environment, commands, viewport, observed result, and evidence. Re-run the focused check after any authorized fix.

## Output contract

- Separate passed, failed, blocked, and not-run checks.
- Include concise reproduction steps for every failure.
- Name any test files created or changed and the exact commands run.

## Guardrails

- Do not substitute source inspection for browser verification when the claim is visual or interactive.
- Do not use arbitrary timeouts when a deterministic condition is available.
- Do not rewrite the production feature merely to make a brittle test pass.
- Do not perform destructive actions against shared or production environments.

## Failure handling

If the app cannot start or required credentials, services, or fixtures are unavailable, preserve the failure output and report the smallest missing prerequisite. Continue with non-blocked static or unit checks without overstating coverage.
