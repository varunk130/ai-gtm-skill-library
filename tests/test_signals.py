"""Unit tests for python_runtime.signals."""

import pytest

from python_runtime.signals import (
    DEFAULT_WEIGHTS,
    rank_signals,
    score_market_signal,
)


def test_default_weights_sum_to_one():
    assert sum(DEFAULT_WEIGHTS.values()) == pytest.approx(1.0)


def test_zero_features_score_zero_cold():
    s = score_market_signal({})
    assert s.total == 0.0
    assert s.band == "cold"


def test_perfect_features_score_caps_at_100_hot():
    features = {k: 100.0 for k in DEFAULT_WEIGHTS}
    s = score_market_signal(features)
    assert s.total == 100.0
    assert s.band == "hot"


def test_band_thresholds():
    s = score_market_signal({k: 60.0 for k in DEFAULT_WEIGHTS})
    assert s.band == "warm"

    s = score_market_signal({k: 40.0 for k in DEFAULT_WEIGHTS})
    assert s.band == "lukewarm"


def test_missing_features_treated_as_zero():
    s = score_market_signal({"icp_fit": 100.0})
    # only icp_fit (weight 0.25) contributes
    assert s.total == pytest.approx(25.0)


def test_rank_orders_best_first_and_respects_top_n():
    items = [
        ("low", {k: 10.0 for k in DEFAULT_WEIGHTS}),
        ("mid", {k: 50.0 for k in DEFAULT_WEIGHTS}),
        ("high", {k: 90.0 for k in DEFAULT_WEIGHTS}),
    ]
    ranked = rank_signals(items, top_n=2)
    assert [label for label, _ in ranked] == ["high", "mid"]


def test_custom_weights_used_when_provided():
    weights = {"icp_fit": 1.0}
    s = score_market_signal({"icp_fit": 80.0}, weights=weights)
    assert s.total == pytest.approx(80.0)
    assert s.band == "hot"
