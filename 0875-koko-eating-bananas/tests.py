def run(solution):
    solver = solution.Solution()
    assert solver.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert solver.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert solver.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
    assert solver.minEatingSpeed([1], 1) == 1
    assert solver.minEatingSpeed([1000000000], 2) == 500000000
