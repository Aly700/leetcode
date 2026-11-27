class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        size = [1] * len(parent)

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for a, b in edges:
            left, right = find(a), find(b)
            if left == right:
                return [a, b]
            if size[left] < size[right]:
                left, right = right, left
            parent[right] = left
            size[left] += size[right]

        return []
