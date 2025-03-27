class Solution:
    def rob(self, nums: list[int]) -> int:
        def helper(nums: list[int]) -> int:
            rob1, rob2 = 0, 0

            for n in nums:
                new_rob = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = new_rob

            return rob2

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
