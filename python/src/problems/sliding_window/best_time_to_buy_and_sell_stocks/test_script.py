import pytest

from src.problems.sliding_window.best_time_to_buy_and_sell_stocks.script import Solution


@pytest.mark.parametrize(
    "prices, expected_profit",
    [
        ([7, 1, 5, 3, 6, 4], 5),  # Buy at 1, sell at 6
        ([7, 6, 4, 3, 1], 0),  # No profit possible
        ([1, 2, 3, 4, 5], 4),  # Increasing sequence, max profit = last - first
        ([3, 3, 3, 3, 3], 0),  # Same prices every day, no profit
        ([2, 4, 1], 2),  # Buy at 2, sell at 4
        ([1], 0),  # Single element, can't sell
        ([1, 2], 1),  # Buy at 1, sell at 2
        ([5, 4, 3, 2, 1, 10], 9),  # Buy at 1, sell at 10
        ([2, 1, 2, 1, 0, 1, 2], 2),  # Buy at 0, sell at 2
    ],
)
def test_max_profit(prices, expected_profit):
    solution = Solution()
    assert solution.maxProfit(prices) == expected_profit
