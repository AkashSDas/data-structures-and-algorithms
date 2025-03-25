from functools import lru_cache


class Solution:
    def jump(self, nums: list[int]) -> float:
        result = 0
        left, right = 0, 0

        while right < len(nums) - 1:
            farthest = 0

            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])

            left = right + 1
            right = farthest
            result += 1

        return result

    def jump2(self, nums: list[int]) -> float:
        n = len(nums)

        @lru_cache(None)  # Memoization to store results for each index
        def dp(idx: int) -> float:
            if idx >= n - 1:
                return 0  # No more jumps needed when at or past last index

            min_jumps = float("inf")  # Start with a large number

            max_jump = nums[idx]
            for step in range(1, max_jump + 1):
                if idx + step < n:
                    min_jumps = min(min_jumps, 1 + dp(idx + step))

            return min_jumps

        return dp(0)
