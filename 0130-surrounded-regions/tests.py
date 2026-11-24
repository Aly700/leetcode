def check(solver, rows, expected):
    board = [list(row) for row in rows]
    result = solver.solve(board)
    return result is None and board == [list(row) for row in expected]


def run(solution):
    solver = solution.Solution()
    assert check(solver, ["X"], ["X"])
    assert check(solver, ["O"], ["O"])
    assert check(solver, ["XXXX", "XOOX", "XXOX", "XOXX"], ["XXXX", "XXXX", "XXXX", "XOXX"])
    assert check(solver, ["OOO", "OOO", "OOO"], ["OOO", "OOO", "OOO"])
    assert check(solver, ["XXXX", "XOOX", "XOOX", "XXOX"], ["XXXX", "XOOX", "XOOX", "XXOX"])
    assert check(solver, ["OXX", "XOX", "XXO"], ["OXX", "XXX", "XXO"])
    assert check(solver, ["XOXOX"], ["XOXOX"])
    assert check(solver, ["O" * 200 for _ in range(200)], ["O" * 200 for _ in range(200)])
