class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Reverse the matrix vertically
        matrix.reverse()

        # Transpose the matrix
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def rotate2(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                # save the top left value
                top_left = matrix[top][left + i]

                # move bottom left into top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # move bottom right into bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # move top right in to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # move top left into top right
                matrix[top + i][right] = top_left

            left += 1
            right -= 1
