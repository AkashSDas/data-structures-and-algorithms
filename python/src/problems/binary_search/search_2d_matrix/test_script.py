import pytest

from src.problems.binary_search.search_2d_matrix.script import Solution


@pytest.mark.parametrize(
    "matrix, target, expected",
    [
        (
            [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
            3,
            True,
        ),  # Found in first row
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),  # Not present
        (
            [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
            30,
            True,
        ),  # Found in last row
        ([[1, 3, 5, 7]], 5, True),  # Single row matrix, target exists
        ([[1, 3, 5, 7]], 9, False),  # Single row matrix, target not present
        ([[1], [3], [5]], 3, True),  # Single column, target exists
        ([[1], [3], [5]], 4, False),  # Single column, target not present
        ([[1]], 1, True),  # Single element matrix, target exists
        ([[1]], 2, False),  # Single element matrix, target not present
        ([], 1, False),  # Empty matrix
    ],
)
def test_search_matrix(matrix, target, expected):
    solution = Solution()
    assert solution.searchMatrix(matrix, target) == expected
