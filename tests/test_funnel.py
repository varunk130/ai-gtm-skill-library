"""Unit tests for python_runtime.funnel."""

import pytest

from python_runtime.funnel import FunnelStage, analyze_funnel


def test_empty_returns_empty_report():
    report = analyze_funnel([])
    assert report.stages == []
    assert report.overall_conversion == 0.0
    assert report.biggest_drop_stage is None
    assert report.stage_conversions == []


def test_single_stage_overall_is_one():
    report = analyze_funnel([FunnelStage("visit", 100)])
    assert report.overall_conversion == 1.0
    assert report.stage_conversions == []
    assert report.biggest_drop_stage is None


def test_two_stage_conversion():
    report = analyze_funnel([
        FunnelStage("visit", 1000),
        FunnelStage("signup", 250),
    ])
    assert report.overall_conversion == 0.25
    assert report.stage_conversions == [("signup", 0.25)]
    assert report.biggest_drop_stage == "signup"
    assert report.biggest_drop_pct == 0.75


def test_identifies_largest_drop():
    report = analyze_funnel([
        FunnelStage("visit", 1000),
        FunnelStage("signup", 800),
        FunnelStage("activate", 100),
        FunnelStage("paid", 90),
    ])
    assert report.biggest_drop_stage == "activate"
    # signup->activate drop is 1 - 100/800 = 0.875
    assert report.biggest_drop_pct == pytest.approx(0.875, abs=1e-4)


def test_zero_prev_count_safe():
    report = analyze_funnel([
        FunnelStage("visit", 0),
        FunnelStage("signup", 0),
    ])
    assert report.overall_conversion == 0.0
    assert report.stage_conversions == [("signup", 0.0)]


def test_negative_count_raises():
    with pytest.raises(ValueError):
        analyze_funnel([FunnelStage("visit", 100), FunnelStage("signup", -1)])
