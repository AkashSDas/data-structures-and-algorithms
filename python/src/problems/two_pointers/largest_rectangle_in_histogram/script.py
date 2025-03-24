class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack: list[tuple[int, int]] = []

        for i, curr_h in enumerate(heights):

            new_idx = i

            while len(stack) > 0 and stack[-1][1] > curr_h:
                idx, h = stack.pop()
                max_area = max(max_area, h * (i - idx))
                new_idx = idx

            stack.append((new_idx, curr_h))

        while len(stack) > 0:
            idx, h = stack.pop()
            max_area = max(max_area, h * (len(heights) - idx))

        return max_area

    def largestRectangleArea2(self, heights: list[int]) -> int:
        max_area = 0

        for i in range(0, len(heights)):
            areas = [heights[i]]

            for j in range(i + 1, len(heights)):
                min_h = min(heights[i : j + 1])
                areas.append(min_h * (j - i + 1))

            if max_area < max(areas):
                max_area = max(areas)

        return max_area
