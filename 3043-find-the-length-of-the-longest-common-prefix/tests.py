def run(solution):
    solver = solution.Solution()

    # the two LeetCode examples
    assert solver.longestCommonPrefix([1, 10, 100], [1000]) == 3
    assert solver.longestCommonPrefix([1, 2, 3], [4, 4, 4]) == 0

    # an identical number shares all of its digits
    assert solver.longestCommonPrefix([12345], [12345]) == 5

    # the prefix is measured in digits, not in the size of the number
    assert solver.longestCommonPrefix([565, 5655, 56555], [5654]) == 3

    # a shorter number in arr2 can only match up to its own length
    assert solver.longestCommonPrefix([123456], [12]) == 2

    # the best pair need not be the first pair
    assert solver.longestCommonPrefix([9, 84, 777], [1, 88, 7777]) == 3

    # a shared leading digit counts even when nothing else matches
    assert solver.longestCommonPrefix([21], [25]) == 1

    # single elements with no common digit
    assert solver.longestCommonPrefix([3], [7]) == 0
