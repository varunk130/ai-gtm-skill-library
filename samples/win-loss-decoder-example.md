# Win-Loss Decoder - Worked Example

Pairs with the `win-loss-decoder` skill. Fictional sample: 20 ACME Insight Studio decisions last quarter, $1.2M ARR won and $1.5M ARR lost.

## Pattern table

Share = ARR under the code ÷ total ARR for that outcome. Gap = loss share − win share.

| Code | ARR won | Win share | ARR lost | Loss share | Gap |
|---|:-:|:-:|:-:|:-:|:-:|
| VALUE | $0.20M | 16.7% | $0.45M | 30.0% | **+13.3** |
| FIT | $0.15M | 12.5% | $0.30M | 20.0% | **+7.5** |
| PRICE | $0.10M | 8.3% | $0.15M | 10.0% | +1.7 |
| PROCESS | $0.30M | 25.0% | $0.30M | 20.0% | −5.0 |
| STATUS QUO | $0.20M | 16.7% | $0.15M | 10.0% | −6.7 |
| TRUST | $0.25M | 20.8% | $0.15M | 10.0% | −10.8 |

## Fix plan

| Code | Owner | Action | Target metric |
|---|---|---|---|
| VALUE | Marketing | Build an ROI worksheet from the Northwind reporting-hours data; use it in first calls | VALUE loss share under 20% next quarter |
| FIT | Product | Ship the Snowflake connector named in 4 of 6 FIT losses | FIT loss share under 12% |
| PRICE | Pricing | Review only after VALUE and FIT fixes land; the gap is small | Hold |

**Reading the result:** price shows up in the CRM as the top loss reason, but buyer evidence puts VALUE and FIT ahead of it. Trust is a strength: references and security reviews are why ACME wins.
