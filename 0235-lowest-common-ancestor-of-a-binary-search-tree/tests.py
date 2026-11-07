from collections import deque


def build(values, solution):
    if not values or values[0] is None:
        return None
    rest = iter(values[1:])
    root = solution.TreeNode(values[0])
    queue = deque([root])
    while queue:
        node = queue.popleft()
        left = next(rest, None)
        if left is not None:
            node.left = solution.TreeNode(left)
            queue.append(node.left)
        right = next(rest, None)
        if right is not None:
            node.right = solution.TreeNode(right)
            queue.append(node.right)
    return root


def to_level(root):
    values = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            values.append(None)
            continue
        values.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while values and values[-1] is None:
        values.pop()
    return values


def find(root, value):
    if root is None:
        return None
    if root.val == value:
        return root
    return find(root.left, value) or find(root.right, value)


def run(solution):
    solver = solution.Solution()
    root = build([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], solution)
    assert solver.lowestCommonAncestor(root, find(root, 2), find(root, 8)).val == 6
    assert solver.lowestCommonAncestor(root, find(root, 2), find(root, 4)).val == 2
    assert solver.lowestCommonAncestor(root, find(root, 3), find(root, 5)).val == 4
    small = build([2, 1], solution)
    assert solver.lowestCommonAncestor(small, find(small, 2), find(small, 1)).val == 2
