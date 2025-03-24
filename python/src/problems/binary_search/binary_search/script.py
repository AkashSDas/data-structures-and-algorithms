class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start_idx = 0
        end_idx = len(nums) - 1
        print("Started")

        while start_idx <= end_idx:
            print(f"{nums=}, {target=}, {end_idx=}, {start_idx=}")
            mid_idx = start_idx + (end_idx - start_idx) // 2

            if nums[mid_idx] == target:
                return mid_idx
            elif target > nums[mid_idx]:
                start_idx = mid_idx + 1
            else:
                end_idx = mid_idx - 1

        return -1
