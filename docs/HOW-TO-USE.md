<div align="center">

# How to Use the AI GTM Skill Library

A practical guide for getting started with Claude Code and GitHub Copilot

</div>

---

## What Are Skills?

Skills are structured instruction files that teach your AI coding assistant how to perform a specific task. When you install a skill, your assistant gains a new capability: it knows _what_ to produce, _how_ to structure the output, and _which_ frameworks to follow.

Think of each skill as a senior GTM strategist that you can call on by name.

---

## Getting Started

### Prerequisites

| Requirement | Details |
|-------------|---------|
| AI Assistant | Claude Code (Anthropic) or GitHub Copilot (GitHub) |
| Python | 3.9+ (only needed for the installer utility or PowerPoint generation) |
| Git | Any recent version for cloning the repository |

### Step 1: Clone the Repository

```bash
git clone https://github.com/varunk130/ai-gtm-skill-library.git
```

### Step 2: Install Skills

**Option A: Use the Python installer**
```bash
# Install all 31 skills (both clusters) to Claude Code
python scripts/install.py install --platform claude

# Install all skills to GitHub Copilot
python scripts/install.py install --platform copilot

# Install a single skill (the installer searches both clusters)
python scripts/install.py install --skill signal-radar    --platform claude
python scripts/install.py install --skill customer-success --platform claude
```

**Option B: Copy manually**

For Claude Code:
```bash
cp -r ai-gtm-skill-library/gtm-skills/*    ~/.claude/skills/
cp -r ai-gtm-skill-library/revops-skills/* ~/.claude/skills/
```

For GitHub Copilot:
```bash
cp -r ai-gtm-skill-library/gtm-skills/*    .github/skills/
cp -r ai-gtm-skill-library/revops-skills/* .github/skills/
```

### Step 3: Start Using Skills

Once installed, simply ask your assistant to use a skill by name or describe what you need.

---

## How to Invoke a Skill

### In Claude Code

Open Claude Code in your terminal and reference a skill naturally:

| What You Say | Skill That Runs |
|-------------|----------------|
| "Run signal-radar for the cloud security market" | Signal Radar (PULSE) |
| "Create a GTM plan for our new API product" | GTM Exec Plan (PRIME) |
| "Build a competitive battle card vs. Competitor X" | Battle Scanner (ARMOR) |
| "Generate a positioning framework for our platform" | Position Lock (PRISM) |
| "What channels should we prioritize for developer audiences?" | Demand Engine (WAVE) |

### In GitHub Copilot

In Copilot Chat (VS Code, GitHub.com, or CLI), reference skills the same way. If skills are installed in `.github/skills/`, Copilot will pick them up from your repository context.

**Example prompts:**
```text
@workspace Run the market-analyzer skill for the AI developer tools market

@workspace Use the gtm-exec-plan skill to create a GTM strategy for
our new ACME Insight Studio extension targeting enterprise IT teams

@workspace Run battle-scanner against Company A, Company B, and Company C
```

---

## Frequently Asked Questions

### General

**Q: Do I need all 31 skills installed to use one?**
No. Each skill works independently. Some skills produce outputs that enrich downstream skills, but you only need to install the ones you actually use.

**Q: What format are the outputs?**
Most skills produce structured Markdown files. The GTM Exec Plan and Competitive Exec Brief also generate PowerPoint (.pptx) files. All outputs are saved to an `outputs/` directory.

**Q: Can I customize a skill?**
Yes. Each skill is a single Markdown file (`SKILL.md`). Open it, edit the framework, sections, or prompts, and save. Your changes take effect immediately.

---

### Using Skills Together

**Q: What order should I run skills in?**
Follow the GTM lifecycle phases. Here are the most common sequences:

**New product launch (full cycle):**
```text
signal-radar -> whitespace-finder -> market-analyzer -> position-lock
-> battle-scanner -> demand-engine -> enablement-forge -> launch-command
```

**Quick executive GTM plan:**
```text
gtm-exec-plan  (this orchestrates the others automatically)
```

**Competitive deep dive:**
```text
battle-scanner -> competitive-exec-brief -> position-lock
```

**Q: Does one skill automatically call another?**
Not automatically. You run each skill explicitly. However, skills like `gtm-exec-plan` are designed to pull from other skills' outputs if they exist, or generate lightweight inline versions if they do not.

---

### Troubleshooting

**Q: The assistant does not seem to recognize my skill.**
- Verify the skill file is in the correct directory (`~/.claude/skills/` or `.github/skills/`)
- Check that the file is named `SKILL.md` (case-sensitive on some systems)
- Restart your AI assistant session after installing new skills

**Q: PowerPoint generation is not working.**
- Install python-pptx: `pip install python-pptx`
- Ensure Python 3.9+ is available in your PATH
- Deck generation is built into the deck-producing skills (`gtm-exec-plan`, `competitive-exec-brief`) and uses `scripts/generate_sample_deck.py` as a reference implementation — no separate skill install is required

**Q: I get very generic outputs.**
- Provide specific inputs: product name, target audience, competitors, timeline
- The more context you give, the more tailored the output
- Reference prior skill outputs when running downstream skills (e.g., "Use the positioning from my earlier position-lock run")

---

### Platform-Specific

**Q: What is the difference between Claude Code and GitHub Copilot skills?**
The skill files are identical. The only difference is where you install them:

| Platform | Install Path | How It Loads |
|----------|-------------|-------------|
| Claude Code | `~/.claude/skills/<skill>/SKILL.md` | Loaded automatically from your user skills directory |
| GitHub Copilot | `.github/skills/<skill>/SKILL.md` | Loaded from repository context via `@workspace` |

**Q: Can I use skills in GitHub Copilot on github.com?**
Yes. If the skills are committed to your repository under `.github/skills/`, Copilot Chat on github.com can reference them when you use `@workspace` or open the repository context.

---

## Quick reference card

### GTM lifecycle skills (21)

| Task | Skill | Framework |
|---|---|---|
| Detect market signals and trends | signal-radar | PULSE |
| Find market gaps and opportunities | whitespace-finder | DEPTH |
| Size a market with segment analysis | market-analyzer | SCOPE |
| Map the customer buying journey | journey-architect | 7-GATE |
| Build competitive battle cards | battle-scanner | ARMOR |
| Create a 1-slide competitive exec brief | competitive-exec-brief | SHARP |
| Generate a deal-specific battlecard | competitive-battlecard | BATTLE |
| Lock positioning and messaging | position-lock | PRISM |
| Plan multi-channel demand generation | demand-engine | WAVE |
| Create sales / marketing assets | enablement-forge | CRAFT |
| Design a partner strategy | partner-blueprint | BRIDGE |
| Build PLG / community motions | community-catalyst | LOOP |
| Build an ABM playbook | abm-playbook | TIER |
| Coordinate launch announcements | product-announcement | HERALD |
| Orchestrate a product launch | launch-command | IGNITE |
| Run a post-launch retrospective | launch-debrief | MIRROR |
| Optimize budget allocation | budget-allocator | APEX |
| Build a GTM analytics framework | launch-pulse | VITAL |
| Drive retention and expansion | growth-loop | ANCHOR |
| Audit the full skill system health | flywheel-sync | ORBIT |
| **Create a full GTM plan and deck** | **gtm-exec-plan** | **PRIME** |

### RevOps skills (10)

| Task | Skill | Framework |
|---|---|---|
| Design a CS operating model + health score | customer-success | THRIVE |
| Build cohort retention + engagement scoring | customer-analytics | LENS |
| Run a customer advocacy / reference program | customer-advocacy | AMPLIFY |
| Orchestrate multi-track lead nurture | lead-nurture | NURTURE |
| Design a loyalty / lifecycle program | loyalty-lifecycle | BOND |
| Build a referral program with K-factor math | referral-program | RIPPLE |
| Run a T-180 renewal motion | renewal-orchestration | RENEW |
| Build an ARR waterfall + revenue diagnostics | revenue-analytics | LADDER |
| Build a calibrated revenue forecast | revenue-forecasting | FORECAST |
| Stand up a Voice-of-Customer program | voice-of-customer | ECHO |

---

<div align="center">

**Need help?** Open an issue on the [repository](https://github.com/varunk130/ai-gtm-skill-library/issues) or reach out to [Varun Kulkarni](https://github.com/varunk130).

</div>
