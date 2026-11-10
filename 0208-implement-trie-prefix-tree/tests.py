def run(solution):
    trie = solution.Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True
    assert trie.search("apples") is False
    assert trie.startsWith("b") is False
