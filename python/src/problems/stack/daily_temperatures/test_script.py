import pytest

from src.problems.stack.daily_temperatures.script import Solution


@pytest.mark.parametrize(
    "temperatures, expected",
    [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([90, 80, 70, 60], [0, 0, 0, 0]),  # No future warmer day
        ([50, 50, 50, 50], [0, 0, 0, 0]),  # Constant temperatures
        ([40, 35, 45, 30, 50], [2, 1, 2, 1, 0]),  # Mixed pattern
        ([100], [0]),  # Single temperature edge case
        ([], []),  # Empty input
    ],
)
def test_daily_temperatures(temperatures, expected):
    solution = Solution()
    assert solution.dailyTemperatures(temperatures) == expected
