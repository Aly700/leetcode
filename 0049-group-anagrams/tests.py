def _normalize(groups):
    return sorted(sorted(group) for group in groups)


def run(solution):
    solver = solution.Solution()
    got = solver.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert _normalize(got) == _normalize([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    assert _normalize(solver.groupAnagrams([""])) == [[""]]
    assert _normalize(solver.groupAnagrams(["a"])) == [["a"]]
    assert _normalize(solver.groupAnagrams(["ab", "ba", "abc"])) == [["ab", "ba"], ["abc"]]
