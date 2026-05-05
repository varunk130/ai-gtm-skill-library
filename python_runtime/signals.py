"""Market and intent signal scoring helpers for GTM skills."""

from dataclasses import dataclass, field


DEFAULT_WEIGHTS: dict[str, float] = {
    "icp_fit": 0.25,
    "intent_strength": 0.25,
    "buying_committee_size": 0.10,
    "budget_signal": 0.15,
    "timing_signal": 0.15,
    "competitive_displacement": 0.10,
}


@dataclass
class SignalScore:
    total: float
    band: str
    breakdown: dict[str, float] = field(default_factory=dict)


def _band(total: float) -> str:
    if total >= 80:
        return "hot"
    if total >= 60:
        return "warm"
    if total >= 40:
        return "lukewarm"
    return "cold"


def score_market_signal(
    features: dict[str, float],
    weights: dict[str, float] | None = None,
) -> SignalScore:
    """Score a market/intent signal 0..100 from feature -> raw_score (0..100)."""
    weights = weights or DEFAULT_WEIGHTS
    breakdown: dict[str, float] = {}
    total = 0.0
    for k, w in weights.items():
        raw = float(features.get(k, 0.0))
        contribution = round(raw * w, 3)
        breakdown[k] = contribution
        total += contribution
    total = round(min(100.0, max(0.0, total)), 2)
    return SignalScore(total=total, band=_band(total), breakdown=breakdown)


def rank_signals(
    items: list[tuple[str, dict[str, float]]],
    weights: dict[str, float] | None = None,
    top_n: int | None = None,
) -> list[tuple[str, SignalScore]]:
    """Score a list of (label, features) and return ranked best-to-worst."""
    scored = [(label, score_market_signal(feat, weights)) for label, feat in items]
    scored.sort(key=lambda kv: kv[1].total, reverse=True)
    if top_n is not None:
        scored = scored[:top_n]
    return scored
