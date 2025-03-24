import pytest

from src.problems.arrays_and_hashing.two_sum.script import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3, 4], 10, [-1, -1]),  # No solution case
        ([], 5, [-1, -1]),  # Empty list case
    ],
)
def test_two_sum(nums, target, expected):
    solution = Solution()
    assert sorted(solution.twoSum(nums, target)) == sorted(expected)
