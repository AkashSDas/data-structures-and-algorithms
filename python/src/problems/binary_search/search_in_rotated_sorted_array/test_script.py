import pytest

from src.problems.binary_search.search_in_rotated_sorted_array.script import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),  # Target found
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),  # Target not found
        ([1], 0, -1),  # Single-element, target not found
        ([1], 1, 0),  # Single-element, target found
        ([3, 1], 1, 1),  # Two-element rotated, target found
        ([3, 1], 2, -1),  # Two-element rotated, target not found
        ([5, 6, 7, 8, 9, 1, 2, 3], 1, 5),  # Large rotated, target found
        ([5, 6, 7, 8, 9, 1, 2, 3], 4, -1),  # Large rotated, target not found
        ([6, 7, 8, 1, 2, 3, 4, 5], 8, 2),  # Found in first half
        ([6, 7, 8, 1, 2, 3, 4, 5], 2, 4),  # Found in second half
        ([4, 5, 6, 7, 8, 9, 10, 0, 1, 2], 10, 6),  # Found at the boundary
        ([4, 5, 6, 7, 8, 9, 10, 0, 1, 2], 11, -1),  # Out of range
    ],
)
def test_search(nums, target, expected):
    solution = Solution()
    assert solution.search(nums, target) == expected
