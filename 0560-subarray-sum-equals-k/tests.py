def run(solution):
    solver = solution.Solution()
    assert solver.subarraySum([1, 1, 1], 2) == 2
    assert solver.subarraySum([1, 2, 3], 3) == 2
    assert solver.subarraySum([1, -1, 0], 0) == 3
    assert solver.subarraySum([1], 0) == 0
    assert solver.subarraySum([-1, -1, 1], 0) == 1
