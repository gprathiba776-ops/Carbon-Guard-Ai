# Deterministic Factor Lookup API

CarbonGuard's production Factor Lookup API is deployed separately at:

`https://carbonguard-factor-api.onrender.com/`

Endpoint: `POST /lookup-factor`

## Contract

Required:
- `scope`
- `activity`
- `unit`
- `year`

Optional:
- `category`
- `fuel_subtype` / `subtype`

Response states:

- `VERIFIED` — exactly one compatible factor
- `REVIEW_REQUIRED` — multiple compatible factors remain
- `FACTOR_NOT_FOUND` — no compatible factor exists

The complete official 2026 factor dataset is the numerical source. This repository does **not** ship a fabricated toy factor table in place of the production dataset.

## Tool boundary

The Factor Resolver calls this service through a Lyzr custom OpenAPI tool. The raw deterministic response is authoritative.
