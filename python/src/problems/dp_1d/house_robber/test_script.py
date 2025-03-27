import pytest

from src.problems.dp_1d.house_robber.script import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 1], 4),  # Rob house 1 and 3 (1 + 3)
        ([2, 7, 9, 3, 1], 12),  # Rob house 1, 3, and 5 (2 + 9 + 1)
        ([2, 1, 1, 2], 4),  # Rob house 1 and 4 (2 + 2)
        ([5, 5, 10, 100, 10, 5], 110),  # Rob house 1, 4, and 6 (5 + 100 + 5)
        ([0, 0, 0, 0, 0], 0),  # No money to rob
        ([10], 10),  # Only one house, rob it
        ([10, 20], 20),  # Two houses, pick the maximum one
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 30),  # Alternate houses (2+4+6+8+10)
        # ([400] * 100, 20000),  # Max input size, alternate houses
    ],
)
def test_rob(nums, expected):
    sol = Solution()
    assert sol.rob(nums) == expected
