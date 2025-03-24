import pytest

from src.problems.two_pointers.three_sum.script import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        ([1, 2, 3, 4, 5], []),
        ([-1, -2, -3, -4, -5], []),
    ],
)
def test_three_sum(nums, expected):
    solution = Solution()
    assert solution.threeSum(nums) == expected
