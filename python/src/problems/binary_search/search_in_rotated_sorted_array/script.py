class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            element = nums[mid]

            if element == target:
                return mid

            if nums[start] <= element:
                if target > element or target < nums[start]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if target < element or target > nums[end]:
                    end = mid - 1
                else:
                    start = mid + 1

        return -1
