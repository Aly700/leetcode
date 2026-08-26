def run(solution):
    solver = solution.Solution()
    assert solver.characterReplacement("ABAB", 2) == 4
    assert solver.characterReplacement("AABABBA", 1) == 4
    assert solver.characterReplacement("AAAA", 0) == 4
    assert solver.characterReplacement("B", 2) == 1
