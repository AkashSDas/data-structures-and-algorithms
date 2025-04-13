class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result: list[int] = []

        if not matrix or not matrix[0]:
            return result

        top_row = 0
        bottom_row = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top_row <= bottom_row and left <= right:
            # Traverse top row
            for i in range(left, right + 1):
                result.append(matrix[top_row][i])
            top_row += 1

            # Traverse right column
            for i in range(top_row, bottom_row + 1):
                result.append(matrix[i][right])
            right -= 1

            # Traverse bottom row (if still within bounds)
            if top_row <= bottom_row:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom_row][i])
                bottom_row -= 1

            # Traverse left column (if still within bounds)
            if left <= right:
                for i in range(bottom_row, top_row - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
