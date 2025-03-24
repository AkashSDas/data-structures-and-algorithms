from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output: list[int] = []
        queue: deque[int] = deque()  # indexes
        left = 0
        right = 0

        while right < len(nums):
            # Pop smaller values from queue
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)

            # Remove left value from window
            if left > queue[0]:
                queue.popleft()

            if (right + 1) >= k:
                output.append(nums[queue[0]])
                left += 1

            right += 1

        return output

    def maxSlidingWindow2(self, nums: list[int], k: int) -> list[int]:
        output: list[int] = []

        for start in range(len(nums) - k + 1):
            end = start + k
            window = nums[start:end]
            output.append(max(window))

        return output
