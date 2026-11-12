def run(solution):
    solver = solution.Solution()
    assert solver.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert solver.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert solver.findMedianSortedArrays([], [1]) == 1.0
    assert solver.findMedianSortedArrays([2], []) == 2.0
    assert solver.findMedianSortedArrays([1, 2], [-1, 3]) == 1.5
    assert solver.findMedianSortedArrays([1, 1, 1], [1, 1]) == 1.0
