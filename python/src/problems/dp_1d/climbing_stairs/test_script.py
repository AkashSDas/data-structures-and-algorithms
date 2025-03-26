import pytest

from src.problems.dp_1d.climbing_stairs.script import Solution


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),  # Only one way to reach step 1
        (2, 2),  # (1+1) or (2)
        (3, 3),  # (1+1+1), (1+2), (2+1)
        (4, 5),  # (1+1+1+1), (1+1+2), (1+2+1), (2+1+1), (2+2)
        (5, 8),  # Fibonacci pattern
        (10, 89),  # Larger case
        (20, 10946),  # Edge case
        (45, 1836311903),  # Maximum constraint
    ],
)
def test_climb_stairs(n, expected):
    sol = Solution()
    assert sol.climbStairs(n) == expected
