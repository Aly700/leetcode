class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        columns = set()
        rising = set()
        falling = set()
        board = []
        result = []

        def place(row):
            if row == n:
                result.append(board[:])
                return

            for col in range(n):
                if col in columns or row + col in rising or row - col in falling:
                    continue
                columns.add(col)
                rising.add(row + col)
                falling.add(row - col)
                board.append("." * col + "Q" + "." * (n - col - 1))
                place(row + 1)
                board.pop()
                columns.remove(col)
                rising.remove(row + col)
                falling.remove(row - col)

        place(0)
        return result
