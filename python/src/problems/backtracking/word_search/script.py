class Solution:
    def __init__(self) -> None:
        self.result = False

    def exist(self, board: list[list[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])
        word_len = len(word)

        def backtrack(row: int, col: int, idx: int) -> bool:
            # Base cases
            if idx == word_len:
                return True
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or board[row][col] != word[idx]
            ):
                return False

            # Mark the cell as visited by temporarily changing its value
            temp = board[row][col]
            board[row][col] = "#"

            # Explore neighbors
            found = (
                backtrack(row + 1, col, idx + 1)
                or backtrack(row - 1, col, idx + 1)
                or backtrack(row, col + 1, idx + 1)
                or backtrack(row, col - 1, idx + 1)
            )

            # Restore the original value
            board[row][col] = temp

            return found

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if backtrack(row, col, 0):
                        return True

        return False

    def exist2(self, board: list[list[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])

        def backtrack(row, col, curr: list[str], path: set[tuple[int, int]]) -> None:
            if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in path:
                if "".join(curr) == word:
                    self.result = True
                return

            char = board[row][col]
            curr.append(char)
            path.add((row, col))

            if "".join(curr) == word:
                self.result = True
                return

            backtrack(row + 1, col, curr.copy(), path.copy())
            backtrack(row - 1, col, curr.copy(), path.copy())
            backtrack(row, col + 1, curr.copy(), path.copy())
            backtrack(row, col - 1, curr.copy(), path.copy())

        for row in range(rows):
            for col in range(cols):
                backtrack(row, col, [], set())

        return self.result
