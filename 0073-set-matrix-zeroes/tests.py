def run(solution):
    solver = solution.Solution()

    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    solver.setZeroes(matrix)
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    solver.setZeroes(matrix)
    assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

    # zero in the first column only: the flag, not the (0,0) marker, must clear it
    matrix = [[1, 2, 3], [0, 5, 6], [7, 8, 9]]
    solver.setZeroes(matrix)
    assert matrix == [[0, 2, 3], [0, 0, 0], [0, 8, 9]]

    # zero in the first row only: (0,0) stays 1, row 0 is cleared through the column markers
    matrix = [[1, 0, 3], [4, 5, 6]]
    solver.setZeroes(matrix)
    assert matrix == [[0, 0, 0], [4, 0, 6]]

    # zero at (0,0) clears both the first row and the first column
    matrix = [[0, 2], [3, 4]]
    solver.setZeroes(matrix)
    assert matrix == [[0, 0], [0, 4]]

    # single row, single column, and no zeroes at all
    matrix = [[1, 0, 3]]
    solver.setZeroes(matrix)
    assert matrix == [[0, 0, 0]]
    matrix = [[1], [0], [3]]
    solver.setZeroes(matrix)
    assert matrix == [[0], [0], [0]]
    matrix = [[1, 2], [3, 4]]
    solver.setZeroes(matrix)
    assert matrix == [[1, 2], [3, 4]]
