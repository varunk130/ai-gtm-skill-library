"""
Validate that every SKILL.md in gtm-skills/ and revops-skills/ has well-formed
YAML frontmatter with the required fields, and that names are unique across
clusters. Used by .github/workflows/validate-skills.yml.

Exits 0 on success, 1 on any validation failure.
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
CLUSTERS = ["gtm-skills", "revops-skills"]
REQUIRED_FIELDS = {"name", "description"}
MIN_DESCRIPTION_LEN = 60


def parse_frontmatter(skill_path: Path) -> dict | None:
    text = skill_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        meta = yaml.safe_load(parts[1])
    except yaml.YAMLError as exc:
        raise ValueError(f"YAML parse error in {skill_path}: {exc}") from exc
    return meta if isinstance(meta, dict) else None


def validate() -> int:
    errors: list[str] = []
    seen_names: dict[str, Path] = {}

    for cluster in CLUSTERS:
        cluster_dir = REPO_ROOT / cluster
        if not cluster_dir.is_dir():
            errors.append(f"missing cluster directory: {cluster}")
            continue
        for skill_dir in sorted(cluster_dir.iterdir()):
            if not skill_dir.is_dir() or skill_dir.name.startswith("_"):
                continue
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                errors.append(f"{cluster}/{skill_dir.name}: missing SKILL.md")
                continue

            try:
                meta = parse_frontmatter(skill_md)
            except ValueError as exc:
                errors.append(str(exc))
                continue
            if meta is None:
                errors.append(f"{skill_md.relative_to(REPO_ROOT)}: missing or invalid frontmatter")
                continue

            missing = REQUIRED_FIELDS - meta.keys()
            if missing:
                errors.append(
                    f"{skill_md.relative_to(REPO_ROOT)}: missing required field(s) {sorted(missing)}"
                )
                continue

            name = meta["name"]
            description = meta["description"]
            folder = skill_dir.name

            if not isinstance(name, str) or name != folder:
                errors.append(
                    f"{skill_md.relative_to(REPO_ROOT)}: name '{name}' must match folder name '{folder}'"
                )
            if not isinstance(description, str) or len(description) < MIN_DESCRIPTION_LEN:
                errors.append(
                    f"{skill_md.relative_to(REPO_ROOT)}: description too short (< {MIN_DESCRIPTION_LEN} chars)"
                )
            if "Use when:" not in (description or ""):
                errors.append(
                    f"{skill_md.relative_to(REPO_ROOT)}: description must include 'Use when:' triggers"
                )

            if isinstance(name, str):
                if name in seen_names:
                    errors.append(
                        f"duplicate skill name '{name}' in "
                        f"{seen_names[name].relative_to(REPO_ROOT)} and {skill_md.relative_to(REPO_ROOT)}"
                    )
                else:
                    seen_names[name] = skill_md

    if errors:
        print(f"\n{len(errors)} validation error(s):", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"OK: validated {len(seen_names)} skills across {len(CLUSTERS)} clusters")
    return 0


if __name__ == "__main__":
    sys.exit(validate())
