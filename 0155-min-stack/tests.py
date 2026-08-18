def run(solution):
    stack = solution.MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    assert stack.getMin() == -3
    stack.pop()
    assert stack.top() == 0
    assert stack.getMin() == -2

    dupes = solution.MinStack()
    dupes.push(1)
    dupes.push(1)
    dupes.pop()
    assert dupes.getMin() == 1
