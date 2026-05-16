# Changelog

All notable changes to the AI GTM Skill Library are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html) where releases are tagged.

## [Unreleased]

### Added
- **RevOps skill cluster** (10 new skills): `customer-success` (THRIVE), `customer-analytics` (LENS), `customer-advocacy` (AMPLIFY), `lead-nurture` (NURTURE), `loyalty-lifecycle` (BOND), `referral-program` (RIPPLE), `renewal-orchestration` (RENEW), `revenue-analytics` (LADDER), `revenue-forecasting` (FORECAST), `voice-of-customer` (ECHO).
- **"What this solves"** opening section in README with problem statement, solution, and audience guide.
- **Sample preview screenshots** (`samples/previews/`) — PNG renderings of the 4 deck slides and 5 brief pages, embedded in `samples/README.md` so GitHub renders the formatted output inline.
- **`samples/README.md`** with a clear pointer to the previews (since GitHub cannot natively preview `.docx` / `.pptx`).
- **`scripts/render_sample_previews.py`** — Word/PowerPoint COM + PyMuPDF script that regenerates the PNG previews from the binary samples.

### Changed
- **Folder structure**: `skills/` renamed to `gtm-skills/`, and `skills/revops/` lifted to top-level `revops-skills/`. Both clusters are now first-class top-level folders.
- **`scripts/install.py`** updated to scan both `gtm-skills/` and `revops-skills/` automatically; `list` action reports cluster per skill.
- **README rewritten**: consolidated three near-duplicate Mermaid diagrams into one tight horizontal lifecycle view; rebuilt the Skills Catalog grouped by phase with all 31 skills; tightened install / installation duplication; removed marketing-style copy.
- **`gtm-exec-plan/SKILL.md`** description updated: generic platform-GTM triggers replace the previous M365 Copilot extensibility trigger.
- **Featured sample** rewritten end-to-end as **ACME Insight Studio** (fictional mock product from ACME Corporation). All numbers, dates, and competitive details are illustrative.

### Removed
- All M365 Copilot extensibility content: sample `.md`, `.docx`, `.pptx`, and the hard-coded references in the brief / deck generator scripts.
- Duplicate `.github/CONTRIBUTING.md`; root `CONTRIBUTING.md` is the single source.
- Redundant "Quick-Start Workflows" section, duplicated install commands, and the bolted-on "RevOps Cluster" mini-section (now in the main catalog).

### Fixed
- Sample generator scripts wrote outputs to `scripts/samples/` instead of the repo's `samples/`; now resolve correctly to repo-root `samples/`.
- README badges linked to anchors that broke when emoji prefixes were removed from headings.

---

## How to update this file

- Add new entries under **[Unreleased]** as work is merged.
- When tagging a release, rename **[Unreleased]** to `[X.Y.Z] — YYYY-MM-DD` and start a fresh **[Unreleased]** section.
- Group entries under `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`.
