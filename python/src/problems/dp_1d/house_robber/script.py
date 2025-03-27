class Solution:
    def rob(self, nums: list[int]) -> int:
        assert nums, "List of nums shouldn't be empty"

        if len(nums) == 1:
            return nums[0]

        # DP array to store max profit at each house
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            # Choose between robbing the current house or skipping it
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]  # The last element contains the max profit

    def rob2(self, nums: list[int]) -> int:
        assert nums, "List of nums shouldn't be empty"

        cache: dict[int, int] = {}

        def dfs(idx: int) -> int:
            if idx >= len(nums):  # Base case: Out of bounds
                return 0
            if idx in cache:  # Memoization check
                return cache[idx]

            # Either rob this house and jump two steps, or skip it
            rob_this = nums[idx] + dfs(idx + 2)
            skip_this = dfs(idx + 1)

            cache[idx] = max(rob_this, skip_this)  # Store best option
            return cache[idx]

        return dfs(0)  # Start DFS from index 0
