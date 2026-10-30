def run(solution):
    solver = solution.Solution()
    assert solver.findMin([3, 4, 5, 1, 2]) == 1
    assert solver.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert solver.findMin([11, 13, 15, 17]) == 11
    assert solver.findMin([2, 1]) == 1
    assert solver.findMin([1]) == 1
