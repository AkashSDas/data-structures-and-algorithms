import pytest
from src.problems.dp_1d.min_cost_climbing_stairs.script import Solution


@pytest.mark.parametrize(
    "cost, expected",
    [
        ([10, 15, 20], 15),  # Start from index 1, total cost = 15
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),  # Minimum path correctly calculated
        ([0, 0, 0, 0], 0),  # Free stairs
        ([10, 1, 10, 1, 10, 1, 10], 3),  # Choose every second step optimally
        ([0, 0, 1, 1, 1, 1, 0, 0, 0], 2),  # Combination of zero and non-zero steps
        (
            [500, 100, 500, 100, 500, 100, 500, 100],
            400,
        ),  # High and low alternating values
        ([999] * 1000, 499500),  # Large input, testing upper limit
    ],
)
def test_min_cost_climbing_stairs(cost, expected):
    sol = Solution()
    assert sol.minCostClimbingStairs(cost) == expected
