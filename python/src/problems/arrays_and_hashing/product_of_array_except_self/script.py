class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        results = [0] * len(nums)

        prefix = 1
        for i in range(0, len(nums)):
            if i == 0:
                results[i] = 1
            else:
                results[i] = prefix

            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                results[i] = results[i]
            else:
                results[i] *= postfix

            postfix *= nums[i]

        return results
