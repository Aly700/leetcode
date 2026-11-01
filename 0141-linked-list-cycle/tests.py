def build(values, pos, solution):
    nodes = [solution.ListNode(value) for value in values]
    for node, following in zip(nodes, nodes[1:]):
        node.next = following
    if nodes and pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None


def run(solution):
    solver = solution.Solution()
    assert solver.hasCycle(build([3, 2, 0, -4], 1, solution)) is True
    assert solver.hasCycle(build([1, 2], 0, solution)) is True
    assert solver.hasCycle(build([1], -1, solution)) is False
    assert solver.hasCycle(build([], -1, solution)) is False
    assert solver.hasCycle(build([1, 2, 3], -1, solution)) is False
