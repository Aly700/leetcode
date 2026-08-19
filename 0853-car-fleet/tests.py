def run(solution):
    solver = solution.Solution()
    assert solver.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert solver.carFleet(10, [3], [3]) == 1
    assert solver.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
