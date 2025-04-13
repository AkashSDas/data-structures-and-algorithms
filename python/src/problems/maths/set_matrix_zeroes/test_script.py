import pytest
from copy import deepcopy

from src.problems.maths.set_matrix_zeroes.script import Solution


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
        (
            [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # No zeroes
        ),
        ([[0, 2, 3], [4, 5, 6], [7, 8, 9]], [[0, 0, 0], [0, 5, 6], [0, 8, 9]]),
        ([[1, 2, 0], [4, 5, 6], [7, 8, 9]], [[0, 0, 0], [4, 5, 0], [7, 8, 0]]),
        ([[1]], [[1]]),
        ([[0]], [[0]]),
        ([[1, 0]], [[0, 0]]),
        ([[1], [0]], [[0], [0]]),
    ],
)
def test_set_zeroes(matrix, expected):
    sol = Solution()
    matrix_copy = deepcopy(matrix)  # to avoid modifying input data
    sol.setZeroes(matrix_copy)
    assert matrix_copy == expected
