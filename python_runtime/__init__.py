"""Python runtime for the AI GTM Skill Library.

The skills are declarative Markdown contracts; this small runtime
provides reusable scoring helpers (signal detection, funnel analysis)
that skill executors can call into.
"""

from .signals import (
    SignalScore,
    score_market_signal,
    rank_signals,
)
from .funnel import (
    FunnelStage,
    FunnelReport,
    analyze_funnel,
)

__all__ = [
    "SignalScore",
    "score_market_signal",
    "rank_signals",
    "FunnelStage",
    "FunnelReport",
    "analyze_funnel",
]
