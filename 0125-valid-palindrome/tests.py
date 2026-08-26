def run(solution):
    solver = solution.Solution()
    assert solver.isPalindrome("A man, a plan, a canal: Panama") is True
    assert solver.isPalindrome("race a car") is False
    assert solver.isPalindrome(" ") is True
    assert solver.isPalindrome("0P") is False
    assert solver.isPalindrome("ab_a") is True
