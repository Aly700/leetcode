def run(solution):
    solver = solution.Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert solver.exist([row[:] for row in board], "ABCCED") is True
    assert solver.exist([row[:] for row in board], "SEE") is True
    assert solver.exist([row[:] for row in board], "ABCB") is False
    assert solver.exist([["a"]], "a") is True
    assert solver.exist([["a", "a"]], "aaa") is False
