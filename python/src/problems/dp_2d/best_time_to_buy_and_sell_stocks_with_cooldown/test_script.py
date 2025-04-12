import pytest

from src.problems.dp_2d.best_time_to_buy_and_sell_stocks_with_cooldown.script import (
    Solution,
)


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    assert solution.maxProfit([1, 2, 3, 0, 2]) == 3  # [buy, sell, cooldown, buy, sell]


def test_example_2(solution):
    assert solution.maxProfit([1]) == 0  # Not enough days to sell


def test_alternating_prices(solution):
    assert solution.maxProfit([1, 2, 1, 2, 1, 2]) == 2  # buy/sell pairs with cooldown


def test_descending_prices(solution):
    assert solution.maxProfit([5, 4, 3, 2, 1]) == 0  # Never profitable to buy/sell


def test_ascending_prices(solution):
    assert solution.maxProfit([1, 2, 3, 4, 5]) == 4  # buy at 1, sell at 5


def test_single_price(solution):
    assert solution.maxProfit([10]) == 0


def test_empty_prices(solution):
    assert solution.maxProfit([]) == 0
