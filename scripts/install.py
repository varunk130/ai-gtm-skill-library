"""
AI GTM Skill Library - Skill Installer

A lightweight utility to install skills into your Claude Code
or GitHub Copilot environment.
"""

import os
import shutil
import argparse
from pathlib import Path


SKILLS_DIR = Path(__file__).parent / "skills"

CLAUDE_TARGET = Path.home() / ".claude" / "skills"
COPILOT_TARGET = Path(".github") / "skills"

PLATFORMS = {
    "claude": CLAUDE_TARGET,
    "copilot": COPILOT_TARGET,
}


def list_skills():
    """List all available skills in the library."""
    skills = sorted(d.name for d in SKILLS_DIR.iterdir() if d.is_dir())
    print(f"\nAvailable skills ({len(skills)}):\n")
    for skill in skills:
        print(f"  - {skill}")
    print()


def install_skill(skill_name, platform="claude"):
    """Install a single skill to the target platform directory."""
    source = SKILLS_DIR / skill_name
    if not source.exists():
        print(f"Error: Skill '{skill_name}' not found.")
        return False

    target = PLATFORMS[platform] / skill_name
    target.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target, dirs_exist_ok=True)
    print(f"Installed '{skill_name}' to {target}")
    return True


def install_all(platform="claude"):
    """Install all skills to the target platform directory."""
    skills = sorted(d.name for d in SKILLS_DIR.iterdir() if d.is_dir())
    count = 0
    for skill in skills:
        if install_skill(skill, platform):
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
