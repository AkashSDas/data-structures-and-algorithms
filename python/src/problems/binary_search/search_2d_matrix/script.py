class Solution:
    def search_row(self, nums: list[int], target: int) -> bool:
        start_idx = 0
        end_idx = len(nums) - 1

        while start_idx <= end_idx:
            mid_idx = start_idx + (end_idx - start_idx) // 2
            element = nums[mid_idx]

            if target == element:
                return True
            elif target > element:
                start_idx = mid_idx + 1
            else:
                end_idx = mid_idx - 1

        return False

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        start_idx = 0
        end_idx = len(matrix) - 1

        while start_idx <= end_idx:
            mid_idx = start_idx + (end_idx - start_idx) // 2
            mid_row = matrix[mid_idx]

            if target >= mid_row[0] and target <= mid_row[-1]:
                return self.search_row(mid_row, target)
            elif target > mid_row[-1]:
                start_idx = mid_idx + 1
            else:
                end_idx = mid_idx - 1

        return False
