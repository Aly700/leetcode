def run(solution):
    words = solution.WordDictionary()
    words.addWord("bad")
    words.addWord("dad")
    words.addWord("mad")
    assert words.search("pad") is False
    assert words.search("bad") is True
    assert words.search(".ad") is True
    assert words.search("b..") is True
    assert words.search("b") is False
    assert words.search("....") is False
    assert words.search("...") is True
