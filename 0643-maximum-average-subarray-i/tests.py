def _close(a, b):
    return abs(a - b) < 1e-5


def run(solution):
    solver = solution.Solution()
    assert _close(solver.findMaxAverage([1, 12, -5, -6, 50, 3], 4), 12.75)
    assert _close(solver.findMaxAverage([5], 1), 5.0)
    assert _close(solver.findMaxAverage([0, 4, 0, 3, 2], 1), 4.0)
    assert _close(solver.findMaxAverage([-1], 1), -1.0)
    assert _close(solver.findMaxAverage([4, 0, 4, 3, 3], 5), 2.8)
