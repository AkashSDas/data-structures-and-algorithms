import pytest

from src.problems.dp_2d.coin_exchange_2.script import Solution


# Test cases
@pytest.mark.parametrize(
    "amount, coins, expected",
    [
        (5, [1, 2, 5], 4),  # 4 ways: [5], [2+2+1], [2+1+1+1], [1+1+1+1+1]
        (3, [2], 0),  # No way to form 3 with only coin 2
        (10, [10], 1),  # Only one way: [10]
        (0, [1, 2, 5], 1),  # One way to make amount 0 (use nothing)
        (1, [1, 2, 3], 1),  # Only one way: [1]
        (4, [1, 2], 3),  # [1x4], [2+2], [2+1+1]
        (100, [1, 5, 10, 25, 50], 292),  # Known test case from leetcode
    ],
)
def test_coin_combinations(amount, coins, expected):
    assert Solution().change(amount, coins) == expected
