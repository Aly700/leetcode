def run(solution):
    solver = solution.Solution()
    assert solver.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solver.twoSum([3, 2, 4], 6) == [1, 2]
    assert solver.twoSum([3, 3], 6) == [0, 1]
    assert solver.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]
