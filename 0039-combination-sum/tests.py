def run(solution):
    solver = solution.Solution()
    assert sorted(solver.combinationSum([2, 3, 6, 7], 7)) == [[2, 2, 3], [7]]
    assert sorted(solver.combinationSum([2, 3, 5], 8)) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert solver.combinationSum([2], 1) == []
    assert solver.combinationSum([1], 2) == [[1, 1]]
