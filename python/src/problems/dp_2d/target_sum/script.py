from collections import defaultdict


class Solution:

    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        # (0 elements, 0 sum) -> 1 way i.e. 1 way to sum to 0 with first element
        dp[0][0] = 1

        for i in range(len(nums)):
            for curr_sum, count in dp[i].items():
                dp[i + 1][curr_sum + nums[i]] += count
                dp[i + 1][curr_sum - nums[i]] += count

        return dp[len(nums)][target]

    def findTargetSumWays1(self, nums: list[int], target: int) -> int:
        dp = defaultdict(int)

        # (0 sum) -> 1 way i.e. 1 way to sum to 0 with first element
        dp[0] = 1

        for i in range(len(nums)):
            next_dp = defaultdict(int)

            for curr_sum, count in dp.items():
                next_dp[curr_sum + nums[i]] += count
                next_dp[curr_sum - nums[i]] += count

            dp = next_dp

        return dp[target]

    def findTargetSumWays2(self, nums: list[int], target: int) -> int:
        cache: dict[tuple[int, int], int] = {}

        def dfs(idx: int, sum: int) -> int:
            if idx == len(nums):
                if sum == target:
                    return 1
                else:
                    return 0

            if (idx, sum) in cache:
                return cache[(idx, sum)]

            add = dfs(idx + 1, sum + nums[idx])
            subtract = dfs(idx + 1, sum - nums[idx])

            cache[(idx, sum)] = add + subtract
            return cache[(idx, sum)]

        return dfs(0, 0)
