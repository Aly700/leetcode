def run(solution):
    solver = solution.Solution()

    # the two LeetCode examples
    assert solver.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert solver.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
        1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7,
    ]

    assert solver.spiralOrder([[1]]) == [1]
    assert solver.spiralOrder([[1, 2], [3, 4]]) == [1, 2, 4, 3]

    # a single row: once the rightward pass is done the row is spent, so the
    # leftward pass must not walk back over it
    assert solver.spiralOrder([[1, 2, 3]]) == [1, 2, 3]

    # the same guard one turn later, for a single column
    assert solver.spiralOrder([[1], [2], [3]]) == [1, 2, 3]

    # taller than wide, and wider than tall
    assert solver.spiralOrder([[1, 2], [3, 4], [5, 6]]) == [1, 2, 4, 6, 5, 3]
    assert solver.spiralOrder([[1, 2, 3], [4, 5, 6]]) == [1, 2, 3, 6, 5, 4]

    # big enough for a second ring, so the bounds have to close correctly
    assert solver.spiralOrder(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    ) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
