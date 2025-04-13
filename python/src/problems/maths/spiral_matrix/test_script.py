import pytest

from src.problems.maths.spiral_matrix.script import Solution


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
        ([[1]], [1]),
        ([[1, 2], [3, 4]], [1, 2, 4, 3]),
        ([[1], [2], [3], [4]], [1, 2, 3, 4]),
        ([[1, 2, 3, 4]], [1, 2, 3, 4]),
        ([[7, 9], [6, 2], [3, 5]], [7, 9, 2, 5, 3, 6]),
    ],
)
def test_spiral_order(matrix, expected):
    sol = Solution()
    assert sol.spiralOrder(matrix) == expected
