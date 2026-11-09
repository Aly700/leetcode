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
    lists = [build(values, solution) for values in [[1, 4, 5], [1, 3, 4], [2, 6]]]
    assert to_list(solver.mergeKLists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert solver.mergeKLists([]) is None
    assert solver.mergeKLists([None]) is None
    assert to_list(solver.mergeKLists([None, build([2], solution), None, build([1], solution)])) == [1, 2]
