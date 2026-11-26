def run(solution):
    solver = solution.Solution()
    assert solver.canFinish(1, []) is True
    assert solver.canFinish(2, [[1, 0]]) is True
    assert solver.canFinish(2, [[1, 0], [0, 1]]) is False
    assert solver.canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) is True
    assert solver.canFinish(5, [[1, 0], [3, 2], [2, 3]]) is False
    assert solver.canFinish(1, [[0, 0]]) is False
    assert solver.canFinish(2000, [[i, i - 1] for i in range(1, 2000)]) is True
