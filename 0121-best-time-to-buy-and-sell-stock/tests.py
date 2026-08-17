def run(solution):
    solver = solution.Solution()
    assert solver.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert solver.maxProfit([7, 6, 4, 3, 1]) == 0
    assert solver.maxProfit([2, 4]) == 2
