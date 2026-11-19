def valid(boards, n, count):
    if len(boards) != count or len({tuple(board) for board in boards}) != count:
        return False
    for board in boards:
        if len(board) != n or any(len(row) != n or set(row) - {".", "Q"} or row.count("Q") != 1 for row in board):
            return False
        cols = [row.index("Q") for row in board]
        if len(set(cols)) != n or len({r - c for r, c in enumerate(cols)}) != n or len({r + c for r, c in enumerate(cols)}) != n:
            return False
    return True


def run(solution):
    solver = solution.Solution()
    assert valid(solver.solveNQueens(1), 1, 1)
    assert valid(solver.solveNQueens(2), 2, 0)
    assert valid(solver.solveNQueens(3), 3, 0)
    assert valid(solver.solveNQueens(4), 4, 2)
    assert valid(solver.solveNQueens(5), 5, 10)
    assert valid(solver.solveNQueens(6), 6, 4)
    assert valid(solver.solveNQueens(8), 8, 92)
