def run(solution):
    solver = solution.Solution()
    assert sorted(solver.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert solver.topKFrequent([1], 1) == [1]
    assert sorted(solver.topKFrequent([4, 4, 4, 6, 6, 2], 2)) == [4, 6]
