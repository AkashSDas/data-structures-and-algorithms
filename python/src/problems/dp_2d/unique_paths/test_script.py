import pytest

from src.problems.dp_2d.unique_paths.script import Solution


@pytest.mark.parametrize(
    "m, n, expected",
    [
        (3, 7, 28),
        (3, 2, 3),
        (1, 1, 1),  # Only 1 cell, 1 path
        (1, 10, 1),  # Only right moves
        (10, 1, 1),  # Only down moves
        (2, 2, 2),  # Two ways: Right->Down, Down->Right
        (3, 3, 6),  # All combinations of R and D for 2 moves each: C(4,2)=6
    ],
)
def test_unique_paths(m, n, expected):
    assert Solution().uniquePaths(m, n) == expected
