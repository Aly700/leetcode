def run(solution):
    solver = solution.Solution()

    # the two LeetCode examples
    assert solver.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert solver.maxArea([1, 1]) == 1

    # walls of zero height hold nothing
    assert solver.maxArea([0, 0]) == 0

    # strictly increasing, so the widest pair is not the best one
    assert solver.maxArea([1, 2, 3, 4, 5]) == 6

    # flat walls: with nothing to gain in height, width decides
    assert solver.maxArea([5, 5, 5, 5]) == 15

    # a tall adjacent pair beats every wider one — moving the taller
    # pointer instead of the shorter would walk straight past it
    assert solver.maxArea([2, 3, 4, 5, 18, 17, 6]) == 17

    # the short outer walls bound the area, not the tall middle one
    assert solver.maxArea([1, 2, 1]) == 2

    # a lone tall wall is still capped by its short partner
    assert solver.maxArea([1, 10]) == 1
