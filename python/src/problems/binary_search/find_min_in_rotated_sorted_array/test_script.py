import pytest

from src.problems.binary_search.find_min_in_rotated_sorted_array.script import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([4, 5, 6, 7, 0, 1, 2], 0),  # Rotated 4 times
        ([0, 1, 2, 4, 5, 6, 7], 0),  # Not rotated
        ([3, 4, 5, 1, 2], 1),  # Rotated 3 times
        ([11, 13, 15, 17], 11),  # Already sorted, no rotation
        ([2, 1], 1),  # Smallest possible rotated array
        ([1], 1),  # Single-element array
        ([5, 6, 7, 8, 1, 2, 3, 4], 1),  # Rotated at index 4
        ([7, 9, 11, 12, 15, 1, 3, 5], 1),  # Rotated at index 5
        ([2, 3, 4, 5, 6, 7, 8, 9, 1], 1),  # Rotated at last index
    ],
)
def test_find_min(nums, expected):
    solution = Solution()
    assert solution.findMin(nums) == expected
