def run(solution):
    solver = solution.Solution()
    assert solver.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert solver.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert solver.productExceptSelf([2, 2]) == [2, 2]
