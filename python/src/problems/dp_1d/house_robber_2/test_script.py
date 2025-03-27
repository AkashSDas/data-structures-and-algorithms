import pytest

from src.problems.dp_1d.house_robber_2.script import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, 2], 3),  # Cannot rob both first and last house
        ([1, 2, 3, 1], 4),  # Rob house 1 and 3
        ([1, 2, 3], 3),  # Rob house 2 or 3, max is 3
        ([0], 0),  # Single house with no money
        ([5], 5),  # Single house with money
        ([2, 7, 9, 3, 1], 11),  # Max is robbing house 2 and 4
        ([10] * 100, 500),  # Large input, alternating houses for max profit
    ],
)
def test_rob(nums, expected):
    sol = Solution()
    assert sol.rob(nums) == expected
