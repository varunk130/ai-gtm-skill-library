"""
AI GTM Skill Library - Skill Installer

A lightweight utility to install skills into your Claude Code
or GitHub Copilot environment.
"""

import shutil
import argparse
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_SOURCES = [
    REPO_ROOT / "gtm-skills",
    REPO_ROOT / "revops-skills",
]

CLAUDE_TARGET = Path.home() / ".claude" / "skills"
COPILOT_TARGET = Path(".github") / "skills"

PLATFORMS = {
    "claude": CLAUDE_TARGET,
    "copilot": COPILOT_TARGET,
}


def _all_skill_dirs():
    """Yield (skill_name, source_path) for every skill across both clusters."""
    for src in SKILL_SOURCES:
        if not src.exists():
            continue
        for d in sorted(src.iterdir()):
            if d.is_dir() and (d / "SKILL.md").exists():
                yield d.name, d


def _find_skill(skill_name):
    """Locate a skill by name across the configured source directories."""
    for src in SKILL_SOURCES:
        candidate = src / skill_name
        if candidate.exists() and candidate.is_dir():
            return candidate
    return None


def list_skills():
    """List all available skills in the library."""
    skills = list(_all_skill_dirs())
    print(f"\nAvailable skills ({len(skills)}):\n")
    for name, path in skills:
        cluster = path.parent.name
        print(f"  - {name}  ({cluster})")
    print()


def install_skill(skill_name, platform="claude"):
    """Install a single skill to the target platform directory."""
    source = _find_skill(skill_name)
    if source is None:
        print(f"Error: Skill '{skill_name}' not found.")
        return False

    target = PLATFORMS[platform] / skill_name
    target.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target, dirs_exist_ok=True)
    print(f"Installed '{skill_name}' to {target}")
    return True


def install_all(platform="claude"):
    """Install all skills to the target platform directory."""
    count = 0
    for name, _ in _all_skill_dirs():
        if install_skill(name, platform):
            count += 1
    print(f"\nInstalled {count} skills to {PLATFORMS[platform]}")


def main():
    parser = argparse.ArgumentParser(
        description="AI GTM Skill Library Installer"
    )
    parser.add_argument(
        "action",
        choices=["list", "install"],
        help="Action to perform",
    )
    parser.add_argument(
        "--skill",
        help="Skill name to install (omit for all)",
    )
    parser.add_argument(
        "--platform",
        choices=["claude", "copilot"],
        default="claude",
        help="Target platform (default: claude)",
    )

    args = parser.parse_args()

    if args.action == "list":
        list_skills()
    elif args.action == "install":
        if args.skill:
            install_skill(args.skill, args.platform)
        else:
            install_all(args.platform)


if __name__ == "__main__":
    main()


def main():
    parser = argparse.ArgumentParser(
        description="AI GTM Skill Library Installer"
    )
    parser.add_argument(
        "action",
        choices=["list", "install"],
        help="Action to perform",
    )
    parser.add_argument(
        "--skill",
        help="Skill name to install (omit for all)",
    )
    parser.add_argument(
        "--platform",
        choices=["claude", "copilot"],
        default="claude",
        help="Target platform (default: claude)",
    )

    args = parser.parse_args()

    if args.action == "list":
        list_skills()
    elif args.action == "install":
        if args.skill:
            install_skill(args.skill, args.platform)
        else:
            install_all(args.platform)


if __name__ == "__main__":
    main()
