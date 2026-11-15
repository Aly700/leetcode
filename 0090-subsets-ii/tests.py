def normalize(subsets):
    return sorted(sorted(subset) for subset in subsets)


def run(solution):
    solver = solution.Solution()
    assert normalize(solver.subsetsWithDup([0])) == [[], [0]]
    assert normalize(solver.subsetsWithDup([1, 2, 2])) == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    assert normalize(solver.subsetsWithDup([2, 2, 2])) == [[], [2], [2, 2], [2, 2, 2]]
    assert normalize(solver.subsetsWithDup([2, 1])) == [[], [1], [1, 2], [2]]
    assert normalize(solver.subsetsWithDup([-1, -1, 0])) == [[], [-1], [-1, -1], [-1, -1, 0], [-1, 0], [0]]
    assert normalize(solver.subsetsWithDup([1, 2, 1])) == [[], [1], [1, 1], [1, 1, 2], [1, 2], [2]]
