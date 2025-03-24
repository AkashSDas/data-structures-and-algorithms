import pytest

from src.problems.stack.car_fleet.script import Solution


@pytest.mark.parametrize(
    "target, position, speed, expected",
    [
        (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3),  # Example 1
        (10, [3], [3], 1),  # Example 2 (Single car)
        (100, [0, 2, 4], [4, 2, 1], 1),  # Example 3 (All cars merge)
        (10, [], [], 0),  # Edge case: No cars
        (15, [14, 13, 12, 11], [1, 1, 1, 1], 4),  # No fleet merging
        (20, [0, 10, 15], [4, 2, 1], 1),  # All cars merge
        (200, [180, 160, 140, 120, 100], [2, 4, 6, 8, 10], 1),  # One big fleet
    ],
)
def test_car_fleet(target, position, speed, expected):
    solution = Solution()
    assert solution.carFleet(target, position, speed) == expected
