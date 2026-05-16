# 🔄 RevOps Skills Cluster

Ten skills covering the post-sale and revenue-engine surface area of GTM. These complement the existing pre-sale, launch, and amplification skills in this library.

## Skills in this cluster

| # | Skill | Framework | Theme |
|---|-------|-----------|-------|
| 1 | [customer-success](./customer-success/SKILL.md) | `THRIVE` | Coverage model, health scoring, risk playbooks, expansion motion |
| 2 | [customer-analytics](./customer-analytics/SKILL.md) | `LENS` | Lifecycle, engagement scoring, NRR decomposition, segment behavior |
| 3 | [customer-advocacy](./customer-advocacy/SKILL.md) | `AMPLIFY` | Reference / case study / review pipeline + influence attribution |
| 4 | [lead-nurture](./lead-nurture/SKILL.md) | `NURTURE` | Multi-track nurture, scoring, MQL→SQL handoff, cold-lead revival |
| 5 | [loyalty-lifecycle](./loyalty-lifecycle/SKILL.md) | `BOND` | Tiered loyalty, lifecycle journeys, retention economics |
| 6 | [referral-program](./referral-program/SKILL.md) | `RIPPLE` | Viral loop design, K-factor, fraud / cannibalization controls |
| 7 | [renewal-orchestration](./renewal-orchestration/SKILL.md) | `RENEW` | T-180 risk scoring, multi-thread engagement, expansion-at-renewal |
| 8 | [revenue-analytics](./revenue-analytics/SKILL.md) | `LADDER` | ARR waterfall, leading indicators, drivers, CAC payback |
| 9 | [revenue-forecasting](./revenue-forecasting/SKILL.md) | `FORECAST` | Bottoms-up + tops-down ensemble + calibration loop |
| 10 | [voice-of-customer](./voice-of-customer/SKILL.md) | `ECHO` | Multi-source signal, theming, prioritization, loop closure |

## Suggested workflows

### Renewal-quarter run
```
revenue-analytics → customer-analytics → customer-success → renewal-orchestration → revenue-forecasting
```

### Retention engine build
```
customer-analytics → customer-success → voice-of-customer → loyalty-lifecycle → growth-loop
```

### Demand → handoff
```
demand-engine → lead-nurture → enablement-forge → customer-success
```

### Customer-led growth
```
customer-success → customer-advocacy → referral-program → community-catalyst
```

## Install

```bash
# Install only the RevOps cluster (10 skills)
cp -r revops-skills/* ~/.claude/skills/

# Or use the installer to grab one
python scripts/install.py install --skill customer-success --platform claude
```
