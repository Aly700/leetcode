def run(solution):
    solver = solution.Solution()
    assert solver.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
    assert solver.nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]
    assert solver.nextGreaterElement([1], [1]) == [-1]
