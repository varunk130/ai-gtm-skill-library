# Funnel Analysis — Worked Example

Pairs with `python_runtime/funnel.py` and the `budget-allocator` skill.

```python
from python_runtime import FunnelStage, analyze_funnel

stages = [
    FunnelStage("visit",   10_000),
    FunnelStage("signup",   2_400),
    FunnelStage("activate",   620),
    FunnelStage("trial",      210),
    FunnelStage("paid",        58),
]

report = analyze_funnel(stages)
print(report.overall_conversion)     # 0.0058
print(report.biggest_drop_stage)     # 'activate'
print(report.biggest_drop_pct)       # 0.7417
```

**Reading the result**

- Overall visit → paid conversion is 0.58%.
- The biggest single drop is **signup → activate** (74%): three out of four signups never reach first value.
- Recommended next step: feed `biggest_drop_stage` into the `budget-allocator` skill and reallocate spend from top-of-funnel acquisition into onboarding/activation experiments.
