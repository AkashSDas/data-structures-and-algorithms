import pytest
from copy import deepcopy

from src.problems.graph.surround_regions.script import Solution


@pytest.mark.parametrize(
    "input_board, expected_board",
    [
        # Example case
        (
            [
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"],
            ],
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"],
            ],
        ),
        # Single cell
        (
            [["X"]],
            [["X"]],
        ),
        (
            [["O"]],
            [["O"]],
        ),
        # All 'O's
        (
            [["O", "O"], ["O", "O"]],
            [["O", "O"], ["O", "O"]],
        ),
        # All 'X's
        (
            [["X", "X"], ["X", "X"]],
            [["X", "X"], ["X", "X"]],
        ),
        # Surrounded region
        (
            [["X", "X", "X", "X"], ["X", "O", "X", "X"], ["X", "X", "X", "X"]],
            [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"]],
        ),
        # Large board stress test (simple pattern)
        (
            [["O"] * 50]
            + [["O"] + ["X"] * 48 + ["O"] for _ in range(48)]
            + [["O"] * 50],
            [["O"] * 50]
            + [["O"] + ["X"] * 48 + ["O"] for _ in range(48)]
            + [["O"] * 50],
        ),
    ],
)
def test_solve(input_board, expected_board):
    sol = Solution()
    board_copy = deepcopy(input_board)  # Avoid mutating original input
    sol.solve(board_copy)
    assert board_copy == expected_board
