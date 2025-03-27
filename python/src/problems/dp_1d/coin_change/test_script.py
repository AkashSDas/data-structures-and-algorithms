import pytest

from src.problems.dp_1d.coin_change.script import Solution


@pytest.mark.parametrize(
    "coins, amount, expected",
    [
        ([1, 2, 5], 11, 3),  # 11 = 5 + 5 + 1
        ([2], 3, -1),  # Cannot make 3 using only 2s
        ([1], 0, 0),  # Amount is 0, so no coins needed
        ([1], 2, 2),  # 2 = 1 + 1
        ([186, 419, 83, 408], 6249, 20),  # Large case
        ([3, 5, 7], 4, -1),  # No valid combination
        ([3, 5, 7], 10, 2),  # 10 = 5 + 5
        ([2, 5, 10, 1], 27, 4),  # 27 = 10 + 10 + 5 + 2
        ([1, 6, 10], 12, 2),  # 12 = 6 + 6 (fewer coins)
        ([2, 3, 5], 7, 2),  # 7 = 2 + 5
        ([1, 4, 5], 8, 2),  # 8 = 4 + 4
    ],
)
def test_coin_change(coins, amount, expected):
    sol = Solution()
    assert sol.coinChange(coins, amount) == expected
