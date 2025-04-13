import pytest

from src.problems.dp_2d.target_sum.script import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([1, 1, 1, 1, 1], 3, 5),  # Example from prompt
        ([1], 1, 1),  # Only one way to make target
        ([1, 2, 3], 0, 2),  # +1+2-3, +1-2+3
        ([0, 0, 0, 0, 0], 0, 32),  # 2^5 = 32 ways to make 0 with 5 zeros
        ([1000], -1000, 1),  # Only one way: -1000
        ([1, 2, 7, 9, 981], 1000000000, 0),  # Impossible target
        ([1, 2], 3, 1),  # +1+2
        ([1, 2], 1, 1),  # +2-1
    ],
)
def test_find_target_sum_ways(nums, target, expected):
    assert Solution().findTargetSumWays(nums, target) == expected
