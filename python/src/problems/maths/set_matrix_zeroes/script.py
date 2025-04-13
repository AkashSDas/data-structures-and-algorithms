class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        is_first_row_zero = False

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0

                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        is_first_row_zero = True

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for row in range(len(matrix)):
                matrix[row][0] = 0

        if is_first_row_zero:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0

    def setZeroes2(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows: set[int] = set()
        cols: set[int] = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    rows.add(row)
                    cols.add(col)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in rows or col in cols:
                    matrix[row][col] = 0
