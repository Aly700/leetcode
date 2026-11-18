def run(solution):
    solver = solution.Solution()
    assert solver.partition("a") == [["a"]]
    assert sorted(solver.partition("aab")) == [["a", "a", "b"], ["aa", "b"]]
    assert sorted(solver.partition("aa")) == [["a", "a"], ["aa"]]
    assert sorted(solver.partition("aba")) == [["a", "b", "a"], ["aba"]]
    assert sorted(solver.partition("abba")) == [["a", "b", "b", "a"], ["a", "bb", "a"], ["abba"]]
    assert sorted(solver.partition("aaa")) == [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]
    assert solver.partition("abc") == [["a", "b", "c"]]
