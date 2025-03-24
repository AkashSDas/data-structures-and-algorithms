class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(row: int, col: int) -> None:
            row_out_of_range = row < 0 or row >= rows
            col_out_of_range = col < 0 or col >= cols
            out_of_range = row_out_of_range or col_out_of_range

            if out_of_range or board[row][col] != "O":
                return
            else:
                board[row][col] = "-"

                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(row=0, col=c)

            if board[rows - 1][c] == "O":
                dfs(row=rows - 1, col=c)

        for r in range(rows):
            if board[r][0] == "O":
                dfs(row=r, col=0)

            if board[r][cols - 1] == "O":
                dfs(row=r, col=cols - 1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "-":
                    board[r][c] = "O"
