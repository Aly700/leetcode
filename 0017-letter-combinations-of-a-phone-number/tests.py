def run(solution):
    solver = solution.Solution()
    assert sorted(solver.letterCombinations("2")) == ["a", "b", "c"]
    assert sorted(solver.letterCombinations("23")) == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert sorted(solver.letterCombinations("7")) == ["p", "q", "r", "s"]
    assert sorted(solver.letterCombinations("9")) == ["w", "x", "y", "z"]
    assert sorted(solver.letterCombinations("79")) == sorted(a + b for a in "pqrs" for b in "wxyz")
    assert sorted(solver.letterCombinations("22")) == sorted(a + b for a in "abc" for b in "abc")
    assert sorted(solver.letterCombinations("9999")) == sorted(a + b + c + d for a in "wxyz" for b in "wxyz" for c in "wxyz" for d in "wxyz")
