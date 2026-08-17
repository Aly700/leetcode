def run(solution):
    solver = solution.Solution()
    assert solver.lengthOfLongestSubstring("abcabcbb") == 3
    assert solver.lengthOfLongestSubstring("bbbbb") == 1
    assert solver.lengthOfLongestSubstring("pwwkew") == 3
    assert solver.lengthOfLongestSubstring("") == 0
