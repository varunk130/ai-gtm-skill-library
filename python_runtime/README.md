# `python_runtime/`

Small, dependency-free Python helpers that GTM skills can call when they need to compute something — funnel conversion math, signal scoring, ranking — rather than asking an LLM to do arithmetic.

The skills themselves are still Markdown specs. These helpers are optional and live here so that:

1. The math is deterministic, testable, and version-controlled
2. Skills that benefit from it (`signal-radar`, `journey-architect`, `revenue-analytics`) can reference a stable API instead of re-deriving formulas in the prompt
3. Tests live under [`tests/`](../tests/) and run on PR via the validate-skills workflow

## Modules

### `funnel.py` — funnel conversion analysis

```python
from python_runtime.funnel import FunnelStage, analyze_funnel

stages = [
    FunnelStage("Lead",        10_000),
    FunnelStage("MQL",          2_500),
    FunnelStage("SQL",            800),
    FunnelStage("Opportunity",    240),
    FunnelStage("Closed-won",      60),
]
report = analyze_funnel(stages)
report.overall_conversion   # 0.006   (60 / 10000)
report.biggest_drop_stage   # "SQL"   (largest single-stage drop)
report.biggest_drop_pct     # 0.68
report.stage_conversions    # [("MQL", 0.25), ("SQL", 0.32), ...]
```

Used by skills that report a funnel and need a defensible "biggest leak" pointer.

### `signals.py` — weighted market / intent signal scoring

```python
from python_runtime.signals import score_market_signal, rank_signals

score = score_market_signal({
    "icp_fit":                 90,
    "intent_strength":         85,
    "buying_committee_size":   70,
    "budget_signal":           60,
    "timing_signal":           80,
    "competitive_displacement": 50,
})
score.total      # 76.5
score.band       # "warm"   (>= 60 = warm, >= 80 = hot)
score.breakdown  # dict of feature -> weighted contribution

# Rank a list of (label, features) tuples
ranked = rank_signals(items, top_n=5)
```

Used by skills that need to compare and prioritize candidate signals (accounts, opportunities, segments) under explicit weights instead of asking the model to "pick the best."

## Defaults and customization

`signals.DEFAULT_WEIGHTS` is editable per use case. Pass a custom `weights` dict to `score_market_signal()` or `rank_signals()` to override.

## Tests

Run with:

```bash
make test           # all tests
pytest tests/test_funnel.py -v
pytest tests/test_signals.py -v
```
