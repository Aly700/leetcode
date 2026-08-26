def run(solution):
    solver = solution.Solution()
    assert solver.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) is True
    assert solver.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) is False
    assert solver.searchMatrix([[1]], 1) is True
    assert solver.searchMatrix([[1]], 2) is False
