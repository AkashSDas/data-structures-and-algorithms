from functools import lru_cache


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        destination = len(nums) - 1

        for idx in range(len(nums) - 1, -1, -1):
            if idx + nums[idx] >= destination:
                destination = idx

        if destination == 0:
            return True
        else:
            return False

    def canJump2(self, nums: list[int]) -> bool:
        @lru_cache(None)
        def dp(idx: int) -> bool:
            if idx >= (len(nums) - 1):
                return True

            max_jump = nums[idx]
            for step in range(1, max_jump + 1):
                if dp(idx + step):
                    return True

            return False

        return dp(0)
