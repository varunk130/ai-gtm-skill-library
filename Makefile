.PHONY: help install install-copilot list test lint validate regen-samples regen-previews clean

PYTHON ?= python

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

install:  ## Install all 31 skills into ~/.claude/skills
	$(PYTHON) scripts/install.py install --platform claude

install-copilot:  ## Install all 31 skills into .github/skills (run from your target repo)
	$(PYTHON) scripts/install.py install --platform copilot

list:  ## List all available skills with their cluster
	$(PYTHON) scripts/install.py list

test:  ## Run pytest against python_runtime helpers
	$(PYTHON) -m pytest tests/ -v

lint validate:  ## Validate SKILL.md frontmatter across both clusters
	$(PYTHON) scripts/validate_skills.py

regen-samples:  ## Regenerate the ACME .docx and .pptx samples
	$(PYTHON) scripts/generate_sample_brief.py
	$(PYTHON) scripts/generate_sample_deck.py

regen-previews:  ## Regenerate the PNG previews in samples/previews/ (Windows + Office only)
	$(PYTHON) scripts/render_sample_previews.py

clean:  ## Remove generated artifacts
	rm -rf __pycache__ .pytest_cache **/__pycache__
