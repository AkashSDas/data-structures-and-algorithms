from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        if not grid:
            return

        rows, cols = len(grid), len(grid[0])

        visited: set[tuple[int, int]] = set()
        queue: deque[tuple[int, int]] = deque()

        def add_cell(row: int, col: int) -> None:
            out_of_range = min(row, col) < 0 or row == rows or col == cols
            is_visited = (row, col) in visited

            if out_of_range or is_visited or grid[row][col] == -1:
                return
            else:
                visited.add((row, col))
                queue.append((row, col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        dist = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist

                add_cell(r + 1, c)
                add_cell(r - 1, c)
                add_cell(r, c + 1)
                add_cell(r, c - 1)

            dist += 1
