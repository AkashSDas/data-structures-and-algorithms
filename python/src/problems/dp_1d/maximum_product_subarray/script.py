class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        curr_min, curr_max = 1, 1

        for num in nums:
            if num == 0:
                curr_min, curr_max = 1, 1
                continue

            tmp = curr_max
            curr_max = max(num * curr_max, num * curr_min, num)
            curr_min = min(num * tmp, num * curr_min, num)
            res = max(curr_max, res)

        return res
