---
name: example-revops-skill
description: 'One-paragraph summary of what this RevOps skill does and the artifact it produces. Use when: comma-separated trigger phrases (e.g., renewal forecast, NRR analysis, CS coverage model, lead routing, ARR waterfall).'
---

# Example RevOps Skill (MNEMONIC Framework)

One-paragraph framing: what post-sale or revenue-engine problem this skill solves, why the existing playbook (CSM gut-feel, rep-rolled forecast, generic NPS dashboard) fails, and what the skill outputs differently.

## Core Principle

**State the single most important rule the skill enforces** — the opinion that separates this from a generic CS / RevOps template (e.g., "leading signals beat lagging metrics," "renewal is won at T-180 not in the redline").

## The MNEMONIC Framework

| Letter | Stage | The Question |
|---|---|---|
| **M** | First stage | What's the leading signal or operating decision? |
| **N** | Second stage | What's the gating threshold or owner? |
| **E** | Third stage | What artifact does this stage produce? |
| **M** | Fourth stage | (continue the mnemonic) |
| **O** | … | … |
| **N** | … | … |
| **I** | … | … |
| **C** | Final stage | Outcome metric (NRR / GRR / pipeline / retention uplift) |

## Process

1. **First step** — what to instrument, what to score, what to escalate
2. **Second step** — codify thresholds, owners, SLAs
3. **Third step** — design the play library or operating cadence
4. **Fourth step** — measurement and feedback loop
5. **Fifth step** — handoff to paired skill

## Output

Save to `outputs/example-revops-skill-[segment]-[YYYY-MM-DD].md`

| Artifact | Description |
|---|---|
| **Operating spec** | The system this skill stands up (scoring, plays, cadence) |
| **Threshold and trigger table** | Signals → owners → SLAs |
| **Measurement plan** | Leading + lagging metrics |
| **Handoff spec** | What the paired skill consumes |

## Tips

1. **Lead with signal, not lagging metric** — RevOps fails when scorecards confirm churn after it's locked in
2. **Every play has an owner and a deadline** — playbooks without ownership rot
3. **Validate against historical data** — model is decoration until back-tested

## Pairs With

- **upstream-revops-skill** — Provides the input data or signal feed
- **downstream-revops-skill** — Consumes the operating spec or measurement output
- **gtm-skill** — Cross-cluster pairing (e.g., `enablement-forge`, `growth-loop`)
