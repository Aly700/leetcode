def run(solution):
    solver = solution.Solution()
    found = sorted(sorted(subset) for subset in solver.subsets([1, 2, 3]))
    assert found == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    assert sorted(solver.subsets([0])) == [[], [0]]
    assert len(solver.subsets([1, 2, 3, 4, 5])) == 32
