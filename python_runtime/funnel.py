"""Funnel conversion analysis helpers for GTM skills."""

from dataclasses import dataclass, field


@dataclass
class FunnelStage:
    name: str
    count: int


@dataclass
class FunnelReport:
    stages: list[FunnelStage] = field(default_factory=list)
    overall_conversion: float = 0.0
    biggest_drop_stage: str | None = None
    biggest_drop_pct: float = 0.0
    stage_conversions: list[tuple[str, float]] = field(default_factory=list)


def analyze_funnel(stages: list[FunnelStage]) -> FunnelReport:
    """Compute step-by-step and overall conversion plus biggest drop."""
    if not stages:
        return FunnelReport()
    if any(s.count < 0 for s in stages):
        raise ValueError("counts must be non-negative")

    stage_conversions: list[tuple[str, float]] = []
    biggest_drop_stage = None
    biggest_drop_pct = 0.0

    for prev, curr in zip(stages, stages[1:]):
        if prev.count == 0:
            conv = 0.0
        else:
            conv = round(curr.count / prev.count, 4)
        stage_conversions.append((curr.name, conv))
        drop = round(1.0 - conv, 4) if prev.count else 0.0
        if drop > biggest_drop_pct:
            biggest_drop_pct = drop
            biggest_drop_stage = curr.name

    top = stages[0].count
    bottom = stages[-1].count
    overall = round(bottom / top, 4) if top else 0.0

    return FunnelReport(
        stages=stages,
        overall_conversion=overall,
        biggest_drop_stage=biggest_drop_stage,
        biggest_drop_pct=biggest_drop_pct,
        stage_conversions=stage_conversions,
    )
