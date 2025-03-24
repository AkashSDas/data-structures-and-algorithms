import pytest

from src.problems.two_pointers.two_sum.script import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),  # Basic case
        ([2, 3, 4], 6, [0, 2]),  # Another valid case
        ([3, 2, 4], 6, [1, 2]),  # Unordered input
        ([1, 5, 3, 7], 10, [2, 3]),  # Random order
        ([1, 2, 3, 4], 10, [-1, -1]),  # No valid pair
        ([5, 6, 7], 8, [-1, -1]),  # No valid pair
    ],
)
def test_two_sum(nums, target, expected):
    solution = Solution()
    assert solution.twoSum(nums, target) == expected
