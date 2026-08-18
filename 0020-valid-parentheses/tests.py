def run(solution):
    solver = solution.Solution()
    assert solver.isValid("()") is True
    assert solver.isValid("()[]{}") is True
    assert solver.isValid("(]") is False
    assert solver.isValid("([)]") is False
    assert solver.isValid("{[]}") is True
    assert solver.isValid("(") is False
    assert solver.isValid("]") is False
