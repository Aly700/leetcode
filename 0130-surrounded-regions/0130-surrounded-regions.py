class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        stack = []

        def save(r, c):
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == "O":
                board[r][c] = "T"
                stack.append((r, c))

        for r in range(rows):
            save(r, 0)
            save(r, cols - 1)
        for c in range(cols):
            save(0, c)
            save(rows - 1, c)

        while stack:
            r, c = stack.pop()
            save(r - 1, c)
            save(r + 1, c)
            save(r, c - 1)
            save(r, c + 1)

        for r in range(rows):
            for c in range(cols):
                board[r][c] = "O" if board[r][c] == "T" else "X"
