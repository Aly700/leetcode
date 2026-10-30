def run(solution):
    solver = solution.Solution()
    assert solver.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert solver.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert solver.search([5], 5) == 0
    assert solver.search([5], -5) == -1
    assert solver.search([2, 5], 5) == 1
