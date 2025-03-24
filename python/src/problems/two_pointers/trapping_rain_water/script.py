class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) == 0:
            return 0

        i = 0
        j = len(height) - 1

        left_max = height[i]
        right_max = height[j]

        capacity = 0

        while i < j:
            if left_max < right_max:
                i += 1
                left_max = max(height[i], left_max)
                capacity += left_max - height[i]
            else:
                j -= 1
                right_max = max(height[j], right_max)
                capacity += right_max - height[j]

        return capacity
