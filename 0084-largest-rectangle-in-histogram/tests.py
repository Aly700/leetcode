def run(solution):
    solver = solution.Solution()
    assert solver.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert solver.largestRectangleArea([2, 4]) == 4
    assert solver.largestRectangleArea([5]) == 5
    assert solver.largestRectangleArea([2, 2, 2, 2]) == 8
    assert solver.largestRectangleArea([5, 4, 3, 2, 1]) == 9
