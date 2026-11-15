def normalize(combinations):
    return sorted(sorted(combination) for combination in combinations)


def run(solution):
    solver = solution.Solution()
    assert normalize(solver.combinationSum2([1], 1)) == [[1]]
    assert solver.combinationSum2([2], 1) == []
    assert normalize(solver.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)) == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    assert normalize(solver.combinationSum2([2, 5, 2, 1, 2], 5)) == [[1, 2, 2], [5]]
    assert normalize(solver.combinationSum2([1, 1, 1, 1], 2)) == [[1, 1]]
    assert solver.combinationSum2([2], 4) == []
    assert normalize(solver.combinationSum2([3, 1, 2], 3)) == [[1, 2], [3]]
