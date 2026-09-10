# CarbonGuard Sustainability Dashboard

The dashboard is intentionally thin: it collects/visualizes evidence and invokes the existing CarbonGuard SuperFlow inference endpoint.

## Rules

- Do not calculate emissions in the frontend.
- Do not embed webhook secrets in browser code.
- Display the workflow's governance state.
- Never convert `REVIEW_REQUIRED`, `FACTOR_NOT_FOUND`, `UNSUPPORTED_CLAIM` or `BLOCKED` into an approved result.
- Surface factor value, factor ID/source, formula and audit lineage where available.
- Label absence of Scope 3 activity as absence of reported activity, not verified zero emissions.
- Use `ISO 14064-3 aligned` unless formal certification/compliance has independently been established.
