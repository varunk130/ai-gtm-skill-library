---
name: example-skill
description: 'One-paragraph summary of what this skill does and the artifact it produces. Use when: comma-separated list of trigger phrases users might say, intent keywords, common questions, related domain terms.'
---

# Example Skill (MNEMONIC Framework)

One-paragraph framing: what problem this skill addresses, why the existing playbook fails, and what the skill outputs differently. Be specific — vague openings produce vague skills.

## Core Principle

**State the single most important rule the skill enforces.** This is the line that prevents the skill from becoming a generic template — it's the opinion the skill embeds.

## The MNEMONIC Framework

| Letter | Stage | The Question |
|---|---|---|
| **M** | First stage | What does the user need to decide here? |
| **N** | Second stage | What's the gating signal or input? |
| **E** | Third stage | What is the explicit output of this stage? |
| **M** | Fourth stage | (continue the mnemonic) |
| **O** | … | … |
| **N** | … | … |
| **I** | … | … |
| **C** | Final stage | What success looks like |

## Process

1. **First step** — what to do, what to ask, what to produce
2. **Second step** — gating decision and artifact
3. **Third step** — synthesis or scoring
4. **Fourth step** — output assembly
5. **Fifth step** — paired-skill handoff

## Output

Save to `outputs/example-skill-[scope]-[YYYY-MM-DD].md`

| Artifact | Description |
|---|---|
| **Primary deliverable** | The main thing the skill produces |
| **Supporting tables** | Decision matrix, scoring table, etc. |
| **Handoff spec** | What the next paired skill needs |

## Tips

1. **One opinion per skill** — don't try to be all things
2. **Tables beat prose** — they're easier to apply and audit
3. **Pair explicitly** — list which skills consume this skill's output

## Pairs With

- **upstream-skill** — Produces the input this skill needs
- **downstream-skill** — Consumes this skill's output
- **adjacent-skill** — Runs in parallel for full coverage
