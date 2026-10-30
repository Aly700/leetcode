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
    assert to_list(solver.reverseList(build([1, 2, 3, 4, 5], solution))) == [5, 4, 3, 2, 1]
    assert to_list(solver.reverseList(build([1, 2], solution))) == [2, 1]
    assert to_list(solver.reverseList(build([1], solution))) == [1]
    assert solver.reverseList(None) is None
