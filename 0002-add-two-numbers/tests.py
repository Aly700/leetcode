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
    assert to_list(solver.addTwoNumbers(build([2, 4, 3], solution), build([5, 6, 4], solution))) == [7, 0, 8]
    assert to_list(solver.addTwoNumbers(build([0], solution), build([0], solution))) == [0]
    assert to_list(solver.addTwoNumbers(build([9, 9, 9, 9, 9, 9, 9], solution), build([9, 9, 9, 9], solution))) == [8, 9, 9, 9, 0, 0, 0, 1]
