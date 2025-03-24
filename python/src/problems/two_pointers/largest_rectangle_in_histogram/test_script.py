import pytest

from src.problems.two_pointers.largest_rectangle_in_histogram.script import Solution


@pytest.mark.parametrize(
    "heights, expected",
    [
        ([2, 1, 5, 6, 2, 3], 10),  # Example case
        ([2, 4], 4),  # Small case
        ([1, 1, 1, 1], 4),  # All same height
        ([6, 2, 5, 4, 5, 1, 6], 12),  # Complex case
        ([0], 0),  # Single zero
        ([1], 1),  # Single element
        ([100, 2, 100], 100),  # Large peak
        ([1, 2, 3, 4, 5], 9),  # Increasing order
        ([5, 4, 3, 2, 1], 9),  # Decreasing order
        ([], 0),  # Empty list
    ],
)
def test_largestRectangleArea(heights, expected):
    solution = Solution()
    assert solution.largestRectangleArea(heights) == expected
