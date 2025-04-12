from functools import lru_cache


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        @lru_cache(maxsize=None)
        def dfs(i: int, holding: bool) -> int:
            if i >= n:
                return 0

            if holding:
                # Option 1: Sell today -> cooldown tomorrow
                sell = prices[i] + dfs(i + 2, False)

                # Option 2: Hold
                skip = dfs(i + 1, True)

                return max(sell, skip)
            else:
                # Option 1: Buy today
                buy = -prices[i] + dfs(i + 1, True)

                # Option 2: Do nothing
                skip = dfs(i + 1, False)

                return max(buy, skip)

        return dfs(0, False)

    def __init__(self) -> None:
        self.cache: dict[tuple[int, int], int] = {}
        self.max_profit = 0

    def maxProfit2(self, prices: list[int]) -> int:
        def calculate_profit(idx: int, profit: int) -> int:
            if idx >= len(prices):
                return profit

            if (idx, profit) in self.cache:
                return self.cache[(idx, profit)]

            max_curr_profit = profit

            for buy_idx in range(idx, len(prices)):
                for sell_idx in range(buy_idx + 1, len(prices)):
                    curr_profit = prices[sell_idx] - prices[buy_idx]
                    if curr_profit < 0:
                        continue

                    total_profit = calculate_profit(sell_idx + 2, profit + curr_profit)
                    max_curr_profit = max(max_curr_profit, total_profit)

            self.cache[(idx, profit)] = max_curr_profit
            return max_curr_profit

        return calculate_profit(0, 0)
