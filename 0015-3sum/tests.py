def run(solution):
    solver = solution.Solution()
    result = solver.threeSum([-1, 0, 1, 2, -1, -4])
    assert sorted(sorted(t) for t in result) == [[-1, -1, 2], [-1, 0, 1]]
    assert solver.threeSum([0, 1, 1]) == []
    assert solver.threeSum([0, 0, 0]) == [[0, 0, 0]]
