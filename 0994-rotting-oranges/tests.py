def run(solution):
    solver = solution.Solution()

    # the three LeetCode examples
    assert solver.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert solver.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert solver.orangesRotting([[0, 2]]) == 0

    # nothing fresh to begin with: zero minutes, whether or not anything is rotten
    assert solver.orangesRotting([[0]]) == 0
    assert solver.orangesRotting([[2, 2], [2, 0]]) == 0

    # fresh but no rotten source anywhere: never rots
    assert solver.orangesRotting([[1]]) == -1
    assert solver.orangesRotting([[1, 1], [1, 1]]) == -1

    # two sources rot from both ends at once, so the middle finishes in two minutes not four
    assert solver.orangesRotting([[2, 1, 1, 1, 2]]) == 2

    # a minute only counts when something actually rots: the lone rotten orange at the
    # end of the queue must not add a trailing minute
    assert solver.orangesRotting([[2, 1, 0, 2]]) == 1

    # a fresh orange walled off by empty cells stays fresh
    assert solver.orangesRotting([[2, 0, 1]]) == -1

    # single column and a longer path
    assert solver.orangesRotting([[2], [1], [1], [1]]) == 3
    assert solver.orangesRotting([[2, 1, 1], [1, 1, 1], [0, 1, 2]]) == 2
