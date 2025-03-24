from copy import deepcopy


Board = list[list[str]]


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []

        def backtrack(row, cols, diag1, diag2, board):
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1, cols, diag1, diag2, board)

                # Backtrack
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        empty_board = [["." for _ in range(n)] for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)

        return result


class Solution2:
    def __init__(self) -> None:
        self.invalid = "X"
        self.queen = "Q"
        self.empty = "."

    def build_empty_board(self, n: int) -> Board:
        rows: Board = []

        for _ in range(n):
            row: list[str] = []
            for _ in range(n):
                row.append(self.empty)
            rows.append(row)

        return rows

    def get_available_positions(self, board: Board) -> list[tuple[int, int]]:
        n = len(board)

        valid: list[tuple[int, int]] = []

        for row in range(n):
            for col in range(n):
                if board[row][col] == self.empty:
                    valid.append((row, col))

        return valid

    def mark_invalid_positions(self, board: Board, r: int, c: int) -> None:
        n = len(board)

        for col in range(n):
            if board[r][col] == self.empty:
                board[r][col] = self.invalid

        for row in range(n):
            if board[row][c] == self.empty:
                board[row][c] = self.invalid

        d_r, d_c = r - 1, c - 1
        while d_r >= 0 and d_c >= 0:
            if board[d_r][d_c] == self.empty:
                board[d_r][d_c] = self.invalid

            d_r -= 1
            d_c -= 1

        d_r, d_c = r + 1, c + 1
        while d_r < n and d_c < n:
            if board[d_r][d_c] == self.empty:
                board[d_r][d_c] = self.invalid

            d_r += 1
            d_c += 1

        d_r, d_c = r - 1, c + 1
        while d_r >= 0 and d_c < n:
            if board[d_r][d_c] == self.empty:
                board[d_r][d_c] = self.invalid

            d_r -= 1
            d_c += 1

        d_r, d_c = r + 1, c - 1
        while d_r < n and d_c >= 0:
            if board[d_r][d_c] == self.empty:
                board[d_r][d_c] = self.invalid

            d_r += 1
            d_c -= 1

    def compact_board(self, board: Board) -> list[str]:
        result: list[str] = []

        for row in board:
            result.append(
                "".join(list(map(lambda x: "." if x == self.invalid else x, row)))
            )

        return result

    def solveNQueens(self, n: int) -> list[list[str]]:
        result: list[list[str]] = []
        combinations: set[str] = set()

        def recursion(curr: int, board: Board) -> None:
            if curr == 0:
                result_board = self.compact_board(board)
                if "".join(result_board) not in combinations:
                    result.append(result_board)
                    combinations.add("".join(result_board))
                return

            available_positions = self.get_available_positions(board)
            if len(available_positions) < curr:
                return

            for r, c in available_positions:
                new_board = deepcopy(board)
                new_board[r][c] = self.queen
                self.mark_invalid_positions(new_board, r, c)
                recursion(curr - 1, new_board)

        for r in range(n):
            for c in range(n):
                board = self.build_empty_board(n)
                board[r][c] = self.queen
                self.mark_invalid_positions(board, r, c)

                recursion(n - 1, board)

        return result
