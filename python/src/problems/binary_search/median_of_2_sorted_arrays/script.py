class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # keeping nums1 the smaller array

        x = len(nums1)
        y = len(nums2)
        low = 0
        high = x

        is_even = (x + y) % 2 == 0

        # perform binary search on smaller array

        while low <= high:
            mid_x = (low + high) // 2
            mid_y = (x + y + 1) // 2 - mid_x

            max_left_x = nums1[mid_x - 1] if mid_x > 0 else float("-inf")
            min_right_x = nums1[mid_x] if mid_x < x else float("inf")
            max_left_y = nums2[mid_y - 1] if mid_y > 0 else float("-inf")
            min_right_y = nums2[mid_y] if mid_y < y else float("inf")

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if is_even:
                    return (
                        max(max_left_y, max_left_x) + min(min_right_y, min_right_x)
                    ) / 2
                else:
                    return max(max_left_y, max_left_x)
            elif max_left_x > min_right_y:
                high = mid_x - 1
            else:
                low = mid_x + 1

        return -1
