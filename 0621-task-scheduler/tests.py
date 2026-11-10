def run(solution):
    solver = solution.Solution()
    assert solver.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert solver.leastInterval(["A", "C", "A", "B", "D", "B"], 1) == 6
    assert solver.leastInterval(["A", "A", "A", "B", "B", "B"], 3) == 10
    assert solver.leastInterval(["A"], 0) == 1
