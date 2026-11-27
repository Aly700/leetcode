def valid(order, n, prerequisites):
    if sorted(order) != list(range(n)):
        return False
    position = {course: i for i, course in enumerate(order)}
    return all(position[before] < position[after] for after, before in prerequisites)


def run(solution):
    solver = solution.Solution()
    assert valid(solver.findOrder(1, []), 1, [])
    assert valid(solver.findOrder(2, [[1, 0]]), 2, [[1, 0]])
    assert solver.findOrder(2, [[1, 0], [0, 1]]) == []
    edges = [[1, 0], [2, 0], [3, 1], [3, 2]]
    assert valid(solver.findOrder(4, edges), 4, edges)
    assert solver.findOrder(5, [[1, 0], [3, 2], [2, 3]]) == []
    assert valid(solver.findOrder(4, []), 4, [])
    assert solver.findOrder(3, [[1, 0], [2, 1], [0, 2]]) == []
    chain = [[i, i - 1] for i in range(1, 2000)]
    assert valid(solver.findOrder(2000, chain), 2000, chain)
