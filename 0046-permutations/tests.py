def run(solution):
    solver = solution.Solution()
    assert sorted(solver.permute([1, 2, 3])) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert sorted(solver.permute([0, 1])) == [[0, 1], [1, 0]]
    assert solver.permute([1]) == [[1]]
    assert len(solver.permute([1, 2, 3, 4])) == 24
