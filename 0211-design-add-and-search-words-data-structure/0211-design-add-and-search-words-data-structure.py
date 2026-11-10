class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.end = True

    def search(self, word: str) -> bool:
        def walk(node, i):
            if i == len(word):
                return node.end

            ch = word[i]
            if ch == ".":
                return any(walk(child, i + 1) for child in node.children.values())

            child = node.children.get(ch)
            return child is not None and walk(child, i + 1)

        return walk(self.root, 0)
