from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0

        max_area = 0
        rows, cols = len(grid), len(grid[0])
        visited: set[tuple[int, int]] = set()

        def bfs(row_idx, col_idx) -> int:
            queue: deque[tuple[int, int]] = deque()
            visited.add((row_idx, col_idx))
            queue.append((row_idx, col_idx))

            # Four directions: right, left, down, up
            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

            size = 1

            while queue:
                r, c = queue.popleft()

                for dir_row, dir_col in directions:
                    cell_row = r + dir_row
                    cell_col = c + dir_col

                    inside_row = 0 <= cell_row < rows
                    inside_col = 0 <= cell_col < cols
                    inside_range = inside_row and inside_col

                    not_visited = (cell_row, cell_col) not in visited

                    if inside_range and grid[cell_row][cell_col] == 1 and not_visited:
                        visited.add((cell_row, cell_col))
                        queue.append((cell_row, cell_col))
                        size += 1

            return size

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    size = bfs(r, c)

                    if size > max_area:
                        max_area = size

        return max_area
