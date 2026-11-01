def build(values, solution):
    head = None
    for value in reversed(values):
        head = solution.ListNode(value, head)
    return head


def to_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def run(solution):
    solver = solution.Solution()
    for values, expected in [
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1, 2], [1, 2]),
        ([1], [1]),
    ]:
        head = build(values, solution)
        solver.reorderList(head)
        assert to_list(head) == expected
