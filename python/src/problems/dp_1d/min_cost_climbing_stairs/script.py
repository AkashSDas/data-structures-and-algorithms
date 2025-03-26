class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        if n == 2:  # Directly return the minimum of the two starting steps
            return min(cost[0], cost[1])

        # Initialize two variables to track the previous two step costs
        prev2, prev1 = cost[0], cost[1]

        # DP iteration to find the minimum cost
        for i in range(2, n):
            # Take the min cost of previous two steps
            curr = cost[i] + min(prev1, prev2)
            prev2, prev1 = prev1, curr  # Update for next iteration

        return min(prev1, prev2)  # Minimum cost to reach the top
