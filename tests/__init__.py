"""Make the tests/ directory a discoverable package and ensure the repo
root is on sys.path so tests can import `python_runtime` directly."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
