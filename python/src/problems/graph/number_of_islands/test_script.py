import pytest

from src.problems.graph.number_of_islands.script import Solution


@pytest.mark.parametrize(
    "grid, expected",
    [
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
        ),
        ([["0", "0", "0", "0"], ["0", "0", "0", "0"], ["0", "0", "0", "0"]], 0),
        ([["1", "0", "1", "0"], ["0", "1", "0", "1"], ["1", "0", "1", "0"]], 6),
        ([], 0),
        ([["1"]], 1),
        ([["0"]], 0),
    ],
)
def test_num_islands(grid, expected):
    solution = Solution()
    assert solution.numIslands(grid) == expected
