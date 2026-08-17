def run(solution):
    solver = solution.Solution()
    assert solver.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert solver.twoSum([2, 3, 4], 6) == [1, 3]
    assert solver.twoSum([-1, 0], -1) == [1, 2]
