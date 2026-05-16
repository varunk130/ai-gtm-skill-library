"""
Generate skills-index.json — a machine-readable manifest of every skill in
both gtm-skills/ and revops-skills/ clusters, parsed from each SKILL.md's
YAML frontmatter. Used by anyone who wants to discover or filter skills
programmatically (other tools, websites, dashboards).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT = REPO_ROOT / "skills-index.json"
CLUSTERS = ["gtm-skills", "revops-skills"]


def parse_frontmatter(skill_md: Path) -> dict:
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    meta = yaml.safe_load(parts[1]) or {}
    return meta if isinstance(meta, dict) else {}


def extract_framework(skill_md: Path) -> str | None:
    """Pull the framework name from a heading like '# Skill Name (FRAMEWORK Framework)'."""
    text = skill_md.read_text(encoding="utf-8")
    match = re.search(r"^# .+? \(([A-Z0-9-]+) (?:Framework|Protocol|System)\)", text, re.MULTILINE)
    return match.group(1) if match else None


def extract_use_when(description: str) -> list[str]:
    """Pull the comma-separated 'Use when:' triggers from a description string."""
    if "Use when:" not in description:
        return []
    trail = description.split("Use when:", 1)[1].strip().rstrip(".")
    return [t.strip() for t in trail.split(",") if t.strip()]


def build_index() -> dict:
    clusters_out = []
    total = 0
    for cluster in CLUSTERS:
        cluster_dir = REPO_ROOT / cluster
        if not cluster_dir.is_dir():
            continue
        skills = []
        for skill_dir in sorted(cluster_dir.iterdir()):
            if not skill_dir.is_dir() or skill_dir.name.startswith("_"):
                continue
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue
            meta = parse_frontmatter(skill_md)
            description = str(meta.get("description", ""))
            skills.append({
                "name": meta.get("name", skill_dir.name),
                "framework": extract_framework(skill_md),
                "path": str(skill_md.relative_to(REPO_ROOT)).replace("\\", "/"),
                "description": description,
                "use_when": extract_use_when(description),
            })
        clusters_out.append({
            "name": cluster,
            "skill_count": len(skills),
            "skills": skills,
        })
        total += len(skills)

    return {
        "schema_version": 1,
        "total_skills": total,
        "clusters": clusters_out,
    }


def main() -> int:
    index = build_index()
    OUTPUT.write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(REPO_ROOT)} ({index['total_skills']} skills across {len(index['clusters'])} clusters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
