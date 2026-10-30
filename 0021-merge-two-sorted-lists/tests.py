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
    assert to_list(solver.mergeTwoLists(build([1, 2, 4], solution), build([1, 3, 4], solution))) == [1, 1, 2, 3, 4, 4]
    assert solver.mergeTwoLists(None, None) is None
    assert to_list(solver.mergeTwoLists(None, build([0], solution))) == [0]
    assert to_list(solver.mergeTwoLists(build([5], solution), build([1, 2], solution))) == [1, 2, 5]
