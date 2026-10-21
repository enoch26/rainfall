import pytest

from rainfall.exceptions import EmptyRecordsError
from rainfall.stats import count_wet_days, mean, moving_average, wettest_day
from rainfall.types import Record


def test_count_wet_days_uses_default_threshold(march_records: list[Record]) -> None:
    assert count_wet_days(march_records) == 3


def test_count_wet_days_uses_given_threshold(march_records: list[Record]) -> None:
    assert count_wet_days(march_records, threshold_mm=2.0) == 2


def test_mean_of_three_values() -> None:
    assert mean([1.0, 2.0, 3.0]) == 2.0


@pytest.mark.parametrize("values_mm", [[], ()])
def test_mean_rejects_empty_values(values_mm: list[float] | tuple[float, ...]) -> None:
    with pytest.raises(EmptyRecordsError, match="expected at least one rainfall value"):
        mean(values_mm)


@pytest.mark.parametrize("values_mm", [[0.0], [0.0, 0.0], (2.5,)])
def test_mean_accepts_non_empty_values(
    values_mm: list[float] | tuple[float, ...],
) -> None:
    assert mean(values_mm) == pytest.approx(sum(values_mm) / len(values_mm))


def test_moving_average_returns_values() -> None:
    assert len(moving_average([1.0, 2.0, 3.0, 4.0], 2)) > 0


def test_wettest_day_returns_date_with_most_rain(
    march_records: list[Record],
) -> None:
    assert wettest_day(march_records) == "2026-03-02"


def test_wettest_day_rejects_empty_records() -> None:
    with pytest.raises(EmptyRecordsError):
        wettest_day([])
