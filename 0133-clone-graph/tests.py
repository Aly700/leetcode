def check(solution, solver, adjacency):
    nodes = [solution.Node(i + 1) for i in range(len(adjacency))]
    for node, neighbors in zip(nodes, adjacency):
        node.neighbors = [nodes[i - 1] for i in neighbors]
    root = nodes[0] if nodes else None
    clone = solver.cloneGraph(root)
    if root is None:
        return clone is None
    if clone is None or clone.val != 1:
        return False
    copies = {}
    stack = [clone]
    while stack:
        node = stack.pop()
        if node in nodes or not 1 <= node.val <= len(nodes):
            return False
        if node.val in copies:
            if copies[node.val] is not node:
                return False
            continue
        copies[node.val] = node
        if sorted(neighbor.val for neighbor in node.neighbors) != sorted(adjacency[node.val - 1]):
            return False
        stack.extend(node.neighbors)
    if len(copies) != len(nodes):
        return False
    if [[neighbor.val for neighbor in node.neighbors] for node in nodes] != adjacency:
        return False
    clone.val = -1
    clone.neighbors.clear()
    clone.neighbors.append(clone)
    return root.val == 1 and [node.val for node in root.neighbors] == adjacency[0]


def run(solution):
    solver = solution.Solution()
    assert check(solution, solver, [])
    assert check(solution, solver, [[]])
    assert check(solution, solver, [[2], [1]])
    assert check(solution, solver, [[2, 3], [1, 3], [1, 2]])
    assert check(solution, solver, [[2, 4], [1, 3], [2, 4], [1, 3]])
    assert check(solution, solver, [[2, 3, 4], [1], [1], [1]])
    assert check(solution, solver, [[2], [1, 3], [2, 4], [3]])
