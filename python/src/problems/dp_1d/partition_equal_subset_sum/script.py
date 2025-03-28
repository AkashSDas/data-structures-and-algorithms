class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp: set[int] = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            new_dp = dp.copy()
            for t in dp:
                if t + nums[i] == target:
                    return True

                new_dp.add(t + nums[i])
            dp = new_dp

        return target in dp
