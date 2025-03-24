from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited: set[tuple[int, int]] = set()
        islands = 0

        def bfs(row_idx: int, col_idx: int) -> None:
            queue: deque[tuple[int, int]] = deque()
            visited.add((row_idx, col_idx))
            queue.append((row_idx, col_idx))

            while queue:
                row, col = queue.popleft()

                # Four directions: right, left, down, up
                directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

                for dir_row, dir_col in directions:
                    cell_row = row + dir_row
                    cell_col = col + dir_col

                    inside_row = 0 <= cell_row < rows
                    inside_col = 0 <= cell_col < cols
                    inside_range = inside_row and inside_col

                    not_visited = (cell_row, cell_col) not in visited

                    if inside_range and grid[cell_row][cell_col] == "1" and not_visited:
                        queue.append((cell_row, cell_col))
                        visited.add((cell_row, cell_col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands
