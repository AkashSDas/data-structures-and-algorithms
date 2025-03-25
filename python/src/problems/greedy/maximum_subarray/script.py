class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        result = nums[0]

        curr_sum = 0

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += num
            result = max(curr_sum, result)

        return result

    def maxSubArrayDivideAndConquer(self, nums: list[int]) -> float:
        def helper(left: int, right: int) -> float:
            if left == right:
                return nums[left]  # Base case: single element

            mid = (left + right) // 2

            left_max = helper(left, mid)  # Max sum in left half
            right_max = helper(mid + 1, right)  # Max sum in right half
            cross_max = self.maxCrossingSum(nums, left, mid, right)  # Cross sum

            return max(left_max, right_max, cross_max)

        return helper(0, len(nums) - 1)

    def maxCrossingSum(self, nums: list[int], left: int, mid: int, right: int) -> float:
        # Find max sum on the left side from mid
        left_sum = float("-inf")
        curr_sum = 0
        for i in range(mid, left - 1, -1):
            curr_sum += nums[i]
            left_sum = max(left_sum, curr_sum)

        # Find max sum on the right side from mid+1
        right_sum = float("-inf")
        curr_sum = 0
        for i in range(mid + 1, right + 1):
            curr_sum += nums[i]
            right_sum = max(right_sum, curr_sum)

        return left_sum + right_sum
