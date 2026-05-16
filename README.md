<div align="center">

# 🚀 AI GTM Skill Library

### The 20-Skill AI-Powered Go-To-Market Engine — including the new ABM playbook for Claude Code, GitHub Copilot & Cursor

[![Skills](https://img.shields.io/badge/Skills-19-blue?style=for-the-badge)](#-skills-catalog)
[![Frameworks](https://img.shields.io/badge/Frameworks-19-green?style=for-the-badge)](#-skills-catalog)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![How To Use](https://img.shields.io/badge/How_To_Use-Guide-purple?style=for-the-badge)](docs/HOW-TO-USE.md)
[![Built with Claude Code](https://img.shields.io/badge/Built_with-Claude_Code-D97757?logo=anthropic&logoColor=white&style=for-the-badge)](https://claude.ai/code)
[![GitHub Copilot](https://img.shields.io/badge/GitHub-Copilot-24292e?logo=github&logoColor=white&style=for-the-badge)](https://github.com/features/copilot)

**Created and maintained by [Varun Kulkarni](https://github.com/varunk130)** · [⚡ Quickstart ↓](#-quickstart) · [Skills Catalog ↓](#-skills-catalog) · [How To Use](docs/HOW-TO-USE.md)

**A curated library of skills for Claude Code and GitHub Copilot that gives AI-first GTM teams a structured, repeatable engine for every phase of go-to-market, from early market signal detection through post-launch retrospectives.** Each skill encodes a proprietary framework that transforms your AI coding assistant into a domain-specific GTM strategist, eliminating the gap between insight and execution.

</div>

---

## ⚡ Quickstart

```bash
# 1. Clone the repo
git clone https://github.com/varunk130/ai-gtm-skill-library.git

# 2. Install all 19 skills globally for Claude Code
mkdir -p ~/.claude/skills
cp -r ai-gtm-skill-library/skills/* ~/.claude/skills/

# 3. Restart Claude Code, then run a phase-specific workflow:
#      /signal-radar          — macro-market signal detection
#      /position-lock         — competitive positioning
#      /launch-command        — full launch orchestration
#      /flywheel-sync         — audit health of the entire 18-skill system
```

> 💡 First-time setup, GitHub Copilot integration, and FAQs are in the [How to Use Guide](docs/HOW-TO-USE.md) and the [full Installation](#%EF%B8%8F-installation) section below.

---

## 💡 Why This Matters

> **For AI GTM teams, this library replaces fragmented playbooks and tribal knowledge with 19 composable, AI-native skills that turn strategic analysis into executable plans in minutes, not weeks.** Teams using this system report collapsing their market-to-launch cycle by operationalizing every GTM phase with structured frameworks that build on each other like a flywheel.

---

## 🏗️ Ecosystem Architecture

The skills are organized into **5 strategic phases** that map to the full GTM lifecycle:

```mermaid
flowchart LR
    D["🔍 DISCOVER<br/>signal-radar<br/>whitespace-finder"]
    DE["📐 DESIGN<br/>market-analyzer<br/>journey-architect"]
    P["🎯 POSITION<br/>position-lock<br/>battle-scanner<br/>competitive-exec-brief"]
    L["🚀 LAUNCH<br/>launch-command<br/>product-announcement<br/>launch-debrief"]
    A["📢 AMPLIFY<br/>demand-engine<br/>enablement-forge<br/>partner-blueprint<br/>community-catalyst"]
    O["📊 OPTIMIZE<br/>budget-allocator<br/>launch-pulse<br/>growth-loop"]
    FS["🔄 flywheel-sync<br/>ORBIT system audit<br/>(bottleneck analysis<br/>across all 18)"]

    D --> DE --> P --> L
    L --> A --> O
    O -.-> D
    FS -.-> D
    FS -.-> DE
    FS -.-> P
    FS -.-> L
    FS -.-> A
    FS -.-> O

    classDef discover fill:#0078D4,color:#fff,stroke:#005A9E,stroke-width:2px,rx:8,ry:8
    classDef design fill:#5C2D91,color:#fff,stroke:#412066,stroke-width:2px,rx:8,ry:8
    classDef position fill:#E81123,color:#fff,stroke:#A80000,stroke-width:2px,rx:8,ry:8
    classDef launch fill:#EE7100,color:#fff,stroke:#B85800,stroke-width:2px,rx:8,ry:8
    classDef amplify fill:#107C10,color:#fff,stroke:#0B6A0B,stroke-width:2px,rx:8,ry:8
    classDef optimize fill:#107C10,color:#fff,stroke:#0B6A0B,stroke-width:2px,rx:8,ry:8
    classDef sync fill:#B4009E,color:#fff,stroke:#8C0078,stroke-width:2px,rx:8,ry:8
    class D discover
    class DE design
    class P position
    class L launch
    class A amplify
    class O optimize
    class FS sync
```

---

## 📋 Skills Catalog

| # | Skill | Framework | Phase | Description |
|---|-------|-----------|-------|-------------|
| 1 | Signal Radar | `PULSE` | Discover | Macro-market signal detection: tech shifts, regulatory changes, buyer behavior, ecosystem dynamics |
| 2 | Whitespace Finder | `DEPTH` | Discover | Maps gaps between market demand and existing solutions with opportunity scoring |
| 3 | Market Analyzer | `SCOPE` | Design | Investment-grade market analysis beyond TAM/SAM/SOM with segment deep dives |
| 4 | Journey Architect | `7-GATE` | Design | End-to-end customer journey with gated progression and friction scoring |
| 5 | Battle Scanner | `ARMOR` | Position | Competitive intelligence with response prediction and battle cards |
| 6 | Competitive Exec Brief | `SHARP` | Position | Executive-ready competitive brief with 1-slide PPTX output |
| 7 | Position Lock | `PRISM` | Position | Brand positioning architecture with L0-L5 message cascade |
| 8 | Demand Engine | `WAVE` | Amplify | Multi-channel demand gen strategy with channel scoring and budget allocation |
| 9 | Enablement Forge | `CRAFT` | Amplify | Sales/marketing asset creation from pitch decks to objection handlers |
| 10 | Partner Blueprint | `BRIDGE` | Amplify | Partner strategy: identify, score, and structure partnerships with co-GTM plans |
| 11 | Community Catalyst | `LOOP` | Amplify | PLG and community strategy with viral loops and K-factor modeling |
| 12 | Product Announcement | `HERALD` | Launch | Coordinated multi-channel launch comms from press release to social to internal |
| 13 | Launch Command | `IGNITE` | Launch | Launch orchestration with 8 workstreams, 4 gates, and go/no-go scoring |
| 14 | Budget Allocator | `APEX` | Optimize | Budget optimization with portfolio theory, scenario analysis, experiment reserves |
| 15 | Launch Pulse | `VITAL` | Optimize | GTM analytics architecture: metrics pyramid, dashboards, alerts, attribution |
| 16 | Growth Loop | `ANCHOR` | Optimize | Retention and expansion strategy with health scoring and advocacy programs |
| 17 | Launch Debrief | `MIRROR` | Launch | Post-launch retrospective with 5-Whys root cause and improvement scoring |
| 18 | Flywheel Sync | `ORBIT` | System | Audits health of the entire skill system with bottleneck analysis |
| 19 | **GTM Exec Plan** | **`PRIME`** | **Orchestrator** | **Creates a polished 3-4 page GTM exec brief and a 4-slide PowerPoint deck** |
| 20 | Competitive Battlecard | `BATTLE` | Position | On-demand sales battlecards for live deals: positioning matrix, top objections + responses, trap questions, "do not say" list |

---

## 🔄 Workflow: Full GTM Lifecycle

From first market signal to post-launch optimization, here is how the six phases connect:

```mermaid
flowchart TD
    DISCOVER["🔍 <b>DISCOVER</b><br/>signal-radar<br/>whitespace-finder<br/><br/>Detect market signals<br/>and map opportunity gaps"]

    DESIGN["📐 <b>DESIGN</b><br/>market-analyzer<br/>journey-architect<br/><br/>Size the market and<br/>map the buyer journey"]

    POSITION["🎯 <b>POSITION</b><br/>battle-scanner<br/>competitive-exec-brief<br/>position-lock<br/><br/>Build competitive intel<br/>and lock messaging"]

    AMPLIFY["📢 <b>AMPLIFY</b><br/>demand-engine<br/>enablement-forge<br/>partner-blueprint<br/>community-catalyst<br/><br/>Activate channels, arm sellers,<br/>and mobilize partners"]

    LAUNCH["🚀 <b>LAUNCH</b><br/>product-announcement<br/>launch-command<br/>launch-debrief<br/><br/>Orchestrate launch execution<br/>and run retrospectives"]

    OPTIMIZE["📊 <b>OPTIMIZE</b><br/>budget-allocator<br/>launch-pulse<br/>growth-loop<br/><br/>Optimize spend, measure impact,<br/>and drive retention"]

    DISCOVER ==>|"Opportunity signals"| DESIGN
    DESIGN ==>|"Market & journey insights"| POSITION
    POSITION ==>|"Messaging & competitive edge"| AMPLIFY
    AMPLIFY ==>|"Enabled channels & assets"| LAUNCH
    LAUNCH ==>|"Performance data & learnings"| OPTIMIZE
    OPTIMIZE -.->|"Growth insights feed next cycle"| DISCOVER

    style DISCOVER fill:#0078D4,stroke:#005A9E,color:#fff,rx:12,ry:12
    style DESIGN fill:#00B7C3,stroke:#008B94,color:#fff,rx:12,ry:12
    style POSITION fill:#5C2D91,stroke:#451F6E,color:#fff,rx:12,ry:12
    style AMPLIFY fill:#FF8C00,stroke:#CC7000,color:#fff,rx:12,ry:12
    style LAUNCH fill:#D13438,stroke:#A4262C,color:#fff,rx:12,ry:12
    style OPTIMIZE fill:#107C10,stroke:#0B6A0B,color:#fff,rx:12,ry:12
```

> **Flywheel Sync** (`ORBIT`) operates as a system-wide health layer that audits connections between all six phases, identifies bottlenecks, and generates improvement roadmaps to keep the entire engine running smoothly.

---

## 🎯 Skill Dependency Map

Each skill produces outputs that feed into downstream skills. Here's the data flow:

```mermaid
flowchart TD
    SR[🔍 signal-radar] -->|Market signals| WF[🔍 whitespace-finder]
    WF -->|Opportunity map| MA[📐 market-analyzer]
    MA -->|Market sizing| JA[📐 journey-architect]
    JA -->|Customer journey| BS[🎯 battle-scanner]
    BS -->|Battle cards| CEB[🎯 competitive-exec-brief]
    BS -->|Competitive intel| PL[🎯 position-lock]
    PL -->|Messaging framework| DE[📢 demand-engine]
    PL -->|Positioning| EF[📢 enablement-forge]
    CEB -->|Exec brief| EF
    DE -->|Channel strategy| EF
    DE -->|Demand plan| PB[📢 partner-blueprint]
    PB -->|Partner GTM| CC[📢 community-catalyst]
    EF -->|Sales assets| LC[🚀 launch-command]
    CC -->|Community plan| PA[🚀 product-announcement]
    PA -->|Launch comms| LC
    LC -->|Launch plan| BA[📊 budget-allocator]
    BA -->|Budget model| LP[📊 launch-pulse]
    LP -->|Metrics framework| GL[📊 growth-loop]
    GL -->|Retention insights| LD[🚀 launch-debrief]
    LD -->|Improvements| SR

    FS[🔄 flywheel-sync] -.->|Health audit| SR
    FS -.->|Health audit| LC
    FS -.->|Health audit| GL

    style SR fill:#0078D4,stroke:#005A9E,color:#fff
    style WF fill:#0078D4,stroke:#005A9E,color:#fff
    style MA fill:#00B7C3,stroke:#008B94,color:#fff
    style JA fill:#00B7C3,stroke:#008B94,color:#fff
    style BS fill:#5C2D91,stroke:#451F6E,color:#fff
    style CEB fill:#5C2D91,stroke:#451F6E,color:#fff
    style PL fill:#5C2D91,stroke:#451F6E,color:#fff
    style DE fill:#FF8C00,stroke:#CC7000,color:#fff
    style EF fill:#FF8C00,stroke:#CC7000,color:#fff
    style PB fill:#FF8C00,stroke:#CC7000,color:#fff
    style CC fill:#FF8C00,stroke:#CC7000,color:#fff
    style PA fill:#D13438,stroke:#A4262C,color:#fff
    style LC fill:#D13438,stroke:#A4262C,color:#fff
    style LD fill:#D13438,stroke:#A4262C,color:#fff
    style BA fill:#107C10,stroke:#0B6A0B,color:#fff
    style LP fill:#107C10,stroke:#0B6A0B,color:#fff
    style GL fill:#107C10,stroke:#0B6A0B,color:#fff
    style FS fill:#B4009E,stroke:#8C0078,color:#fff
```

---

## ⚡ Quick-Start Workflows

### 🆕 New Market Entry
```
signal-radar -> whitespace-finder -> market-analyzer -> position-lock -> demand-engine
```

### 🏁 Product Launch
```
battle-scanner -> position-lock -> enablement-forge -> launch-command -> product-announcement -> launch-pulse
```

### 📊 Quarterly Strategy Review
```
flywheel-sync -> signal-radar -> growth-loop -> budget-allocator -> launch-debrief
```

### 🤝 Partner-Led Expansion
```
market-analyzer -> partner-blueprint -> community-catalyst -> demand-engine -> enablement-forge
```

### 📝 Executive GTM Plan
```
gtm-exec-plan  (orchestrates positioning, competitive, channel, and execution planning automatically)
```
Produces a 3-4 page executive brief and a 4-slide PowerPoint deck ready for leadership review.

---

## 🛠️ Installation

> **New to this library?** Read the [How to Use Guide](docs/HOW-TO-USE.md) for step-by-step instructions, example prompts, and FAQs.

Each skill is a standalone `SKILL.md` file that can be installed into your Claude Code or GitHub Copilot environment.

### Claude Code

```bash
# Clone this repo
git clone https://github.com/varunk130/ai-gtm-skill-library.git

# Copy all skills to your Claude Code skills directory
cp -r ai-gtm-skill-library/skills/* ~/.claude/skills/

# Or install a single skill
cp -r ai-gtm-skill-library/skills/signal-radar ~/.claude/skills/
```

### GitHub Copilot

```bash
# Clone this repo
git clone https://github.com/varunk130/ai-gtm-skill-library.git

# Copy all skills to your GitHub Copilot instructions directory
cp -r ai-gtm-skill-library/skills/* .github/skills/

# Or install a single skill
cp -r ai-gtm-skill-library/skills/signal-radar .github/skills/
```

> **Tip:** For GitHub Copilot, you can also reference skills directly from your `.github/copilot-instructions.md` file or include them as custom instructions in your Copilot Chat settings.

### Directory Structure
```
ai-gtm-skill-library/
├── README.md
├── skills/
│   ├── signal-radar/SKILL.md        # PULSE Framework
│   ├── whitespace-finder/SKILL.md   # DEPTH Framework
│   ├── market-analyzer/SKILL.md     # SCOPE Framework
│   ├── journey-architect/SKILL.md   # 7-GATE Framework
│   ├── battle-scanner/SKILL.md      # ARMOR Framework
│   ├── competitive-exec-brief/SKILL.md # SHARP Framework
│   ├── position-lock/SKILL.md       # PRISM Framework
│   ├── demand-engine/SKILL.md       # WAVE Framework
│   ├── enablement-forge/SKILL.md    # CRAFT Framework
│   ├── partner-blueprint/SKILL.md   # BRIDGE Framework
│   ├── community-catalyst/SKILL.md  # LOOP Framework
│   ├── product-announcement/SKILL.md # HERALD Framework
│   ├── launch-command/SKILL.md      # IGNITE Protocol
│   ├── budget-allocator/SKILL.md    # APEX Framework
│   ├── launch-pulse/SKILL.md        # VITAL Framework
│   ├── growth-loop/SKILL.md         # ANCHOR Framework
│   ├── launch-debrief/SKILL.md      # MIRROR Framework
│   ├── flywheel-sync/SKILL.md       # ORBIT System
│   ├── gtm-exec-plan/SKILL.md      # PRIME Framework
│   ├── competitive-battlecard/SKILL.md # BATTLE Framework
├── docs/
│   └── HOW-TO-USE.md
└── LICENSE
```

---

## 🧠 Framework Quick Reference

| Framework | Mnemonic | Core Concept |
|-----------|----------|--------------|
| **PULSE** | _P_attern, _U_npack, _L_ayer, _S_core, _E_scalate | Detect signals before they become obvious |
| **DEPTH** | _D_emand, _E_xisting, _P_ain, _T_rend, _H_ypothesis | Find gaps others miss |
| **SCOPE** | _S_egment, _C_aliber, _O_pportunity, _P_otential, _E_dge | Size markets with conviction |
| **7-GATE** | Seven decision gates across the buyer journey | Design journeys that convert |
| **ARMOR** | _A_nalyze, _R_ank, _M_ap, _O_utmaneuver, _R_espond | Compete with intelligence |
| **SHARP** | _S_napshot, _H_ead-to-head, _A_ction, _R_isk, _P_itch | Brief executives in 60 seconds |
| **PRISM** | _P_osition, _R_eason, _I_mpact, _S_tory, _M_essage | Lock positioning across levels |
| **WAVE** | _W_here, _A_udience, _V_ehicle, _E_xecute | Drive demand across channels |
| **CRAFT** | _C_ontext, _R_ole, _A_sset, _F_ormat, _T_one | Forge assets that enable sellers |
| **BRIDGE** | _B_uild, _R_each, _I_ntegrate, _D_rive, _G_row, _E_valuate | Bridge to partner ecosystems |
| **LOOP** | _L_aunch, _O_nboard, _O_rchestrate, _P_ropagate | Create community viral loops |
| **HERALD** | _H_eadline, _E_cho, _R_each, _A_lign, _L_aunch, _D_istribute | Herald launches across every channel |
| **IGNITE** | 8 workstreams × 4 gates | Orchestrate launches with precision |
| **APEX** | _A_llocate, _P_rioritize, _E_xperiment, _X_-optimize | Optimize budget like a portfolio |
| **VITAL** | _V_isibility, _I_nsight, _T_racking, _A_lert, _L_earn | Build GTM analytics that matter |
| **ANCHOR** | _A_cquire, _N_urture, _C_onvert, _H_old, _O_ptimize, _R_enew | Anchor customers for expansion |
| **MIRROR** | _M_easure, _I_dentify, _R_oot-cause, _R_ecommend, _O_wn, _R_eview | Reflect honestly post-launch |
| **ORBIT** | _O_bserve, _R_ate, _B_ottleneck, _I_mprove, _T_rack | Keep the flywheel spinning |
| **PRIME** | _P_ositioning, _R_eadiness, _I_mpact, _M_otion, _E_xecution | Full GTM plan and deck in one skill |

---

## 🤝 Contributing

We welcome contributions! To add or improve a skill:

1. Fork this repository
2. Create a feature branch (`git checkout -b improve-skill-name`)
3. Update the `SKILL.md` in the relevant skill directory
4. Submit a Pull Request with a description of your changes

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built by Varun Kulkarni**

*Powered by Claude Code & GitHub Copilot*

</div>
