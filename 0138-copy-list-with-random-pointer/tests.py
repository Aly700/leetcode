def build(pairs, solution):
    nodes = [solution.Node(value) for value, _ in pairs]
    for node, following in zip(nodes, nodes[1:]):
        node.next = following
    for node, (_, random_index) in zip(nodes, pairs):
        node.random = nodes[random_index] if random_index is not None else None
    return nodes[0] if nodes else None


def to_pairs(head):
    nodes = []
    node = head
    while node:
        nodes.append(node)
        node = node.next
    index = {id(node): i for i, node in enumerate(nodes)}
    return [[node.val, index[id(node.random)] if node.random else None] for node in nodes]


def run(solution):
    solver = solution.Solution()
    for pairs in [
        [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        [[1, 1], [2, 1]],
        [[3, None], [3, 0], [3, None]],
    ]:
        original = build(pairs, solution)
        copy = solver.copyRandomList(original)
        assert to_pairs(copy) == pairs
        assert copy is not original
        assert copy.next is not original.next
    assert solver.copyRandomList(None) is None
