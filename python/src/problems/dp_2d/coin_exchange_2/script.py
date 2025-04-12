class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        coins.sort()
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[i]:
                    dp[i][a] = dp[i + 1][a]
                    dp[i][a] += dp[i][a - coins[i]]

        return dp[0][amount]

    def change2(self, amount: int, coins: list[int]) -> int:
        cache: dict[tuple[int, int], int] = {}

        def dfs(idx: int, curr_amount: int) -> int:
            if curr_amount == amount:
                return 1
            if curr_amount > amount:
                return 0
            if idx == len(coins):
                return 0
            if (idx, curr_amount) in cache:
                return cache[(idx, curr_amount)]

            result = dfs(idx, curr_amount + coins[idx]) + dfs(idx + 1, curr_amount)
            cache[(idx, curr_amount)] = result
            return result

        return dfs(0, 0)
