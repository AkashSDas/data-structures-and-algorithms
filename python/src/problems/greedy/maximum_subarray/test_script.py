import pytest

from src.problems.greedy.maximum_subarray.script import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),  # Subarray [4,-1,2,1] → Sum = 6
        ([1], 1),  # Single element
        ([5, 4, -1, 7, 8], 23),  # Entire array is max subarray
        ([-1, -2, -3, -4], -1),  # Best single negative number
        ([0, 0, 0, 0], 0),  # All zeroes
        ([3, -1, 4, -1, 2, -5, 4], 7),  # [3,-1,4,-1,2] → Sum = 7
        ([100, -1, -2, 100], 197),  # [100, -1, -2, 100] → Sum = 197
    ],
)
def test_max_subarray_kadane(solution, nums, expected):
    assert solution.maxSubArray(nums) == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-1, -2, -3, -4], -1),
        ([0, 0, 0, 0], 0),
        ([3, -1, 4, -1, 2, -5, 4], 7),
        ([100, -1, -2, 100], 197),
    ],
)
def test_max_subarray_divide_and_conquer(solution, nums, expected):
    assert solution.maxSubArrayDivideAndConquer(nums) == expected
