class Solution:
    def findMin(self, nums: list[int]) -> int:
        result: None | int = None
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            element = nums[mid]

            if result is None:
                result = element
            elif element < result:
                result = element

            if element > nums[-1]:
                start = mid + 1
            else:
                end = mid - 1

        if result is None:
            return -1
        else:
            return result
