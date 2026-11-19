class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        largest = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                grid[r][c] = 0
                stack = [(r, c)]
                area = 0
                while stack:
                    row, col = stack.pop()
                    area += 1
                    for nr, nc in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 0
                            stack.append((nr, nc))
                largest = max(largest, area)

        return largest
