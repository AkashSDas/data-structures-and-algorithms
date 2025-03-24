class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        prev_min = prices[0]
        profit = 0

        for price in prices:
            if price < prev_min:
                prev_min = price

            curr_profit = price - prev_min
            if curr_profit > profit:
                profit = curr_profit

        return profit

    def maxProfit2(self, prices: list[int]) -> int:
        profit = 0
        left = 0
        right = 0

        while right < len(prices):
            print(f"{profit=}, {prices[left]=}, {prices[right]=}")

            if prices[left] < prices[right]:
                profit = max(profit, prices[right] - prices[left])
            else:
                left = right

            right += 1

        return profit
