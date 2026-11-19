def run(solution):
    solver = solution.Solution()
    assert solver.maxAreaOfIsland([[0]]) == 0
    assert solver.maxAreaOfIsland([[1]]) == 1
    assert solver.maxAreaOfIsland([[1, 0], [0, 1]]) == 1
    assert solver.maxAreaOfIsland([[1, 1], [1, 1]]) == 4
    assert solver.maxAreaOfIsland([[1, 1, 0, 1], [0, 1, 0, 1], [1, 0, 0, 1]]) == 3
    assert solver.maxAreaOfIsland([[1, 1, 1, 0, 1]]) == 3
    assert solver.maxAreaOfIsland([[1] * 50 for _ in range(50)]) == 2500
