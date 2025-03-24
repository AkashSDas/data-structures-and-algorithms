import pytest

from src.problems.graph.rotting_oranges.script import Solution


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
        ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
        ([[0, 2]], 0),
        ([[0, 0], [0, 0]], 0),  # No oranges at all
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], -1),  # No rotten oranges, all fresh
        ([[2, 2], [2, 2]], 0),  # All rotten initially
    ],
)
def test_oranges_rotting(grid, expected):
    assert Solution().orangesRotting(grid) == expected
