# Context Anchor - Worked Example

Pairs with the `context-anchor` skill. Fictional product: **ACME Insight Studio**.

## Health table (reviewed 2026-09-19)

| CANVAS section | Completeness (0-2) | Days since review | Freshness |
|---|:-:|:-:|:-:|
| Claim | 2 | 20 | 0.78 |
| Audience | 2 | 45 | 0.50 |
| Need | 1 | 100 | 0.00 |
| Voice | 1 | 10 | 0.89 |
| Alternatives | 2 | 30 | 0.67 |
| Substantiation | 1 | 70 | 0.22 |

- Completeness = 9 / 12 = **0.75**
- Average freshness = 3.06 / 6 = **0.51**
- Context health = 0.75 × 0.51 = **0.38** → below 0.6, so downstream skills warn before running

## Refresh list

| Section | Why | Owner |
|---|---|---|
| Need | Not reviewed in 100 days; trigger events have changed since the Q2 pricing update | Product marketing |
| Substantiation | Two of three customer numbers are from 2025; no evidence attached to the ROI claim | Customer marketing |

**Reading the result:** the claim and audience are solid, but the file would feed stale buying triggers to `trigger-cadence` and unproven numbers to `competitive-battlecard`. Refresh Need and Substantiation first; health rises to about 0.6 once both are reviewed and evidenced.
