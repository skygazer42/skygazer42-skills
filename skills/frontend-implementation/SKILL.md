---
name: frontend-implementation
description: Implement or modify production frontend pages, components, forms, styling, state, and client-side data flows. Use when a user asks to build a UI feature, change interactive behavior, connect an interface to existing APIs, or make a frontend responsive and accessible.
---

# Frontend Implementation

## Workflow

1. Read the request, acceptance criteria, relevant routes, components, styles, tests, and project commands.
2. Trace the real user interaction and data flow before editing. Reuse existing components, tokens, utilities, and installed dependencies.
3. Implement the smallest coherent change. Cover applicable loading, empty, error, success, disabled, and validation states.
4. Preserve semantic HTML, keyboard access, visible focus, labels, useful errors, and responsive behavior.
5. Keep state local unless it is genuinely shared. Avoid unnecessary effects, duplicated derived state, and new dependencies.
6. Run the narrowest relevant type, lint, unit, build, and browser checks available in the repository.
7. Report the behavior delivered, files changed, checks run, and anything not verified.

## Output contract

- Deliver working repository changes, not a detached code sample, when a workspace is available.
- State which acceptance criteria are satisfied.
- Distinguish automated checks from browser or visual verification.

## Guardrails

- Follow the repository's framework and design system; do not replace them for preference.
- Do not add a dependency when the platform, standard library, CSS, or an installed package already covers the need.
- Do not overwrite unrelated user changes or introduce production mock data.
- Do not claim responsive, accessible, or visual correctness without checking it.

## Failure handling

If required behavior cannot be determined from the request or repository, implement only the unambiguous portion and state the exact missing decision. If checks cannot run, give the command attempted and the blocking evidence.
