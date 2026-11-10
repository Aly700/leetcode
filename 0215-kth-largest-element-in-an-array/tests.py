def run(solution):
    solver = solution.Solution()
    assert solver.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert solver.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert solver.findKthLargest([1], 1) == 1
    assert solver.findKthLargest([2, 1], 2) == 1
