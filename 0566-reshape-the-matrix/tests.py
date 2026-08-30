def run(solution):
    solver = solution.Solution()
    assert solver.matrixReshape([[1, 2], [3, 4]], 1, 4) == [[1, 2, 3, 4]]
    assert solver.matrixReshape([[1, 2], [3, 4]], 2, 4) == [[1, 2], [3, 4]]
    assert solver.matrixReshape([[1, 2, 3, 4]], 2, 2) == [[1, 2], [3, 4]]
    assert solver.matrixReshape([[1, 2, 3], [4, 5, 6]], 3, 2) == [[1, 2], [3, 4], [5, 6]]
    assert solver.matrixReshape([[7]], 1, 1) == [[7]]
