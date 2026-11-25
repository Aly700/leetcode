class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def climb(starts):
            reached = set(starts)
            stack = list(reached)
            while stack:
                r, c = stack.pop()
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in reached and heights[nr][nc] >= heights[r][c]:
                        reached.add((nr, nc))
                        stack.append((nr, nc))
            return reached

        pacific = climb([(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)])
        atlantic = climb([(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)])
        return [[r, c] for r, c in pacific & atlantic]
