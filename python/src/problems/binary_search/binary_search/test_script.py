import pytest

from src.problems.binary_search.binary_search.script import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([-1, 0, 3, 5, 9, 12], 9, 4),  # Example 1: Target found
        ([-1, 0, 3, 5, 9, 12], 2, -1),  # Example 2: Target not found
        ([1, 2, 3, 4, 5], 3, 2),  # Target in middle
        ([1, 2, 3, 4, 5], 1, 0),  # Target at beginning
        ([1, 2, 3, 4, 5], 5, 4),  # Target at end
        ([1], 1, 0),  # Single element (found)
        ([1], 2, -1),  # Single element (not found)
        ([], 1, -1),  # Empty list
        ([1, 3, 5, 7, 9, 11], 6, -1),  # Target not in list
    ],
)
def test_search(nums, target, expected):
    solution = Solution()
    assert solution.search(nums, target) == expected
