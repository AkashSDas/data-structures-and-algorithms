class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for amt in range(1, amount + 1):
            for cost in coins:
                if amt - cost >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - cost])

        return dp[amount] if dp[amount] != amount + 1 else -1
