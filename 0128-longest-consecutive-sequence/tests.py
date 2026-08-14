def run(solution):
    solver = solution.Solution()
    assert solver.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert solver.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert solver.longestConsecutive([]) == 0
