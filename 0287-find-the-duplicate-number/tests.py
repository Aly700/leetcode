def run(solution):
    solver = solution.Solution()
    assert solver.findDuplicate([1, 3, 4, 2, 2]) == 2
    assert solver.findDuplicate([3, 1, 3, 4, 2]) == 3
    assert solver.findDuplicate([3, 3, 3, 3, 3]) == 3
    assert solver.findDuplicate([2, 2, 2, 2, 2]) == 2
    assert solver.findDuplicate([1, 1]) == 1
