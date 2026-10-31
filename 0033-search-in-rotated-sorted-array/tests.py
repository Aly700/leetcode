def run(solution):
    solver = solution.Solution()
    assert solver.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert solver.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert solver.search([1], 0) == -1
    assert solver.search([1, 3], 3) == 1
    assert solver.search([3, 1], 1) == 1
    assert solver.search([5, 1, 3], 5) == 0
