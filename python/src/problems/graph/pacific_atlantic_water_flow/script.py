Visited = set[tuple[int, int]]


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific_visited: Visited = set()
        atlantic_visited: Visited = set()

        def dfs(row: int, col: int, visited: Visited, prev_height: int) -> None:
            row_out_of_range = row < 0 or row == rows
            col_out_of_range = col < 0 or col == cols
            out_of_range = row_out_of_range or col_out_of_range

            is_visited = (row, col) in visited

            if out_of_range or heights[row][col] < prev_height or is_visited:
                return
            else:
                visited.add((row, col))

                dfs(row + 1, col, visited, heights[row][col])
                dfs(row - 1, col, visited, heights[row][col])
                dfs(row, col + 1, visited, heights[row][col])
                dfs(row, col - 1, visited, heights[row][col])

        for c in range(cols):
            dfs(
                row=0,
                col=c,
                visited=pacific_visited,
                prev_height=heights[0][c],
            )
            dfs(
                row=rows - 1,
                col=c,
                visited=atlantic_visited,
                prev_height=heights[rows - 1][c],
            )

        for r in range(rows):
            dfs(
                row=r,
                col=0,
                visited=pacific_visited,
                prev_height=heights[r][0],
            )
            dfs(
                row=r,
                col=cols - 1,
                visited=atlantic_visited,
                prev_height=heights[r][cols - 1],
            )

        result: list[list[int]] = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_visited and (r, c) in atlantic_visited:
                    result.append([r, c])

        return result
