def run(solution):
    solver = solution.Solution()
    assert solver.numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]) == 1
    assert solver.numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]) == 3
    assert solver.numIslands([["0"]]) == 0
    assert solver.numIslands([["1"]]) == 1
