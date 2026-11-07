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
    assert solver.isSubtree(build([3, 4, 5, 1, 2], solution), build([4, 1, 2], solution)) is True
    assert solver.isSubtree(build([3, 4, 5, 1, 2, None, None, None, None, 0], solution), build([4, 1, 2], solution)) is False
    assert solver.isSubtree(build([1], solution), build([1], solution)) is True
    assert solver.isSubtree(build([1, 2], solution), build([2], solution)) is True
