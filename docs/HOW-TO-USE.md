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
# Install all skills to Claude Code
python install.py install --platform claude

# Install all skills to GitHub Copilot
python install.py install --platform copilot

# Install a single skill
python install.py install --skill signal-radar --platform claude
```

**Option B: Copy manually**

For Claude Code:
```bash
cp -r ai-gtm-skill-library/skills/* ~/.claude/skills/
```

For GitHub Copilot:
```bash
cp -r ai-gtm-skill-library/skills/* .github/skills/
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
```
@workspace Run the market-analyzer skill for the AI developer tools market

@workspace Use the gtm-exec-plan skill to create a GTM strategy for 
our new M365 Copilot extension targeting enterprise IT teams

@workspace Run battle-scanner against Company A, Company B, and Company C
```

---

## Frequently Asked Questions

### General

**Q: Do I need all 19 skills installed to use one?**
No. Each skill works independently. However, some skills produce outputs that enrich downstream skills. Install only the ones you need.

**Q: What format are the outputs?**
Most skills produce structured Markdown files. The GTM Exec Plan and Competitive Exec Brief also generate PowerPoint (.pptx) files. All outputs are saved to an `outputs/` directory.

**Q: Can I customize a skill?**
Yes. Each skill is a single Markdown file (`SKILL.md`). Open it, edit the framework, sections, or prompts, and save. Your changes take effect immediately.

---

### Using Skills Together

**Q: What order should I run skills in?**
Follow the GTM lifecycle phases. Here are the most common sequences:

**New product launch (full cycle):**
```
signal-radar -> whitespace-finder -> market-analyzer -> position-lock 
-> battle-scanner -> demand-engine -> enablement-forge -> launch-command
```

**Quick executive GTM plan:**
```
gtm-exec-plan  (this orchestrates the others automatically)
```

**Competitive deep dive:**
```
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
- The `ppt-deck-generator` skill handles PPTX creation; ensure it is installed alongside any deck-producing skill

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

## Quick Reference Card

| Task | Skill to Use | Framework |
|------|-------------|-----------|
| Detect market signals and trends | Signal Radar | PULSE |
| Find market gaps and opportunities | Whitespace Finder | DEPTH |
| Size a market with segment analysis | Market Analyzer | SCOPE |
| Map the customer buying journey | Journey Architect | 7-GATE |
| Build competitive battle cards | Battle Scanner | ARMOR |
| Create a 1-slide competitive brief | Competitive Exec Brief | SHARP |
| Lock positioning and messaging | Position Lock | PRISM |
| Plan multi-channel demand generation | Demand Engine | WAVE |
| Create sales and marketing assets | Enablement Forge | CRAFT |
| Design a partner strategy | Partner Blueprint | BRIDGE |
| Build community and PLG motions | Community Catalyst | LOOP |
| Coordinate launch announcements | Product Announcement | HERALD |
| Orchestrate a full product launch | Launch Command | IGNITE |
| Optimize budget allocation | Budget Allocator | APEX |
| Build a GTM analytics framework | Launch Pulse | VITAL |
| Drive retention and expansion | Growth Loop | ANCHOR |
| Run a post-launch retrospective | Launch Debrief | MIRROR |
| Audit the full skill system health | Flywheel Sync | ORBIT |
| **Create a full GTM plan and deck** | **GTM Exec Plan** | **PRIME** |

---

<div align="center">

**Need help?** Open an issue on the [repository](https://github.com/varunk130/ai-gtm-skill-library/issues) or reach out to [Varun Kulkarni](https://github.com/varunk130).

</div>
