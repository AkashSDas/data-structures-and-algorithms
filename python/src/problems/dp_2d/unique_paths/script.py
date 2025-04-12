class Solution:
    def __init__(self) -> None:
        self.paths = 0

    def uniquePaths(self, m: int, n: int) -> int:
        cache: dict[tuple[int, int], int] = {}

        def move(curr_row: int, curr_col: int) -> int:
            if curr_row == m - 1 and curr_col == n - 1:
                return 1

            if curr_row >= m or curr_col >= n:
                return 0

            if (curr_row, curr_col) in cache:
                return cache[(curr_row, curr_col)]

            down_paths = move(curr_row + 1, curr_col)
            right_paths = move(curr_row, curr_col + 1)

            cache[(curr_row, curr_col)] = down_paths + right_paths
            return cache[(curr_row, curr_col)]

        self.paths = move(0, 0)
        return self.paths
