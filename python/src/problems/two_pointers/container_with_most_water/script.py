class Solution:
    def maxArea(self, height: list[int]) -> int:
        area = 0

        left = 0
        right = len(height) - 1

        while left < right:
            min_h = min(height[left], height[right])
            w = right - left
            curr_area = min_h * w

            if curr_area > area:
                area = curr_area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area
