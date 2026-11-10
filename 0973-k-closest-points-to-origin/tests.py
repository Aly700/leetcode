def run(solution):
    solver = solution.Solution()
    assert solver.kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
    assert sorted(solver.kClosest([[3, 3], [5, -1], [-2, 4]], 2)) == [[-2, 4], [3, 3]]
    assert sorted(solver.kClosest([[0, 1], [1, 0]], 2)) == [[0, 1], [1, 0]]
