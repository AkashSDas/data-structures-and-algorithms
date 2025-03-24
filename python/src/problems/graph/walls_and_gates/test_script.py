import pytest

from src.problems.graph.walls_and_gates.script import Solution

INF = 2147483647


@pytest.mark.parametrize(
    "grid, expected",
    [
        (
            [
                [INF, -1, 0, INF],
                [INF, INF, INF, -1],
                [INF, -1, INF, -1],
                [0, -1, INF, INF],
            ],
            [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]],
        ),
        ([[0, -1], [INF, INF]], [[0, -1], [1, 2]]),
        (
            [[-1, INF], [INF, INF]],
            [[-1, INF], [INF, INF]],  # No treasure chests, should remain unchanged
        ),
        ([[0]], [[0]]),  # Single treasure chest
        ([[INF]], [[INF]]),  # Single land, no chest
    ],
)
def test_walls_and_gates(grid, expected):
    Solution().islandsAndTreasure(grid)
    assert grid == expected
