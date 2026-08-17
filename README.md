# leetcode

My LeetCode solve log. A local script pulls my accepted submissions into
problem directories. The index and `problems.json` are generated from those
directories, and every solution runs its example cases in CI.

<!-- INDEX:BEGIN -->
**Solved:** 7 total | 1 easy | 6 medium | 0 hard

| # | Title | Difficulty | Topics | Language |
| ---: | --- | --- | --- | --- |
| 3 | [Longest Substring Without Repeating Characters](0003-longest-substring-without-repeating-characters/0003-longest-substring-without-repeating-characters.py) | Medium | Hash Table, String, Sliding Window | Python (untested) |
| 15 | [3Sum](0015-3sum/0015-3sum.py) | Medium | Array, Two Pointers, Sorting | Python |
| 121 | [Best Time to Buy and Sell Stock](0121-best-time-to-buy-and-sell-stock/0121-best-time-to-buy-and-sell-stock.py) | Easy | Array, Dynamic Programming | Python (untested) |
| 128 | [Longest Consecutive Sequence](0128-longest-consecutive-sequence/0128-longest-consecutive-sequence.py) | Medium | Array, Hash Table, Union-Find | Python |
| 167 | [Two Sum II - Input Array Is Sorted](0167-two-sum-ii-input-array-is-sorted/0167-two-sum-ii-input-array-is-sorted.py) | Medium | Array, Two Pointers, Binary Search | Python |
| 238 | [Product of Array Except Self](0238-product-of-array-except-self/0238-product-of-array-except-self.py) | Medium | Array, Prefix Sum | Python |
| 347 | [Top K Frequent Elements](0347-top-k-frequent-elements/0347-top-k-frequent-elements.py) | Medium | Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect | Python |
<!-- INDEX:END -->

## Adding solutions

Directories may use a numbered name such as `0347-top-k-frequent-elements` or
a plain problem slug. Add `tests.py` with a `run(solution)` function for Python;
the runner imports the solution file and passes its module to that function.
For C++, add `tests_cpp.cpp` with a `main()` containing the cases. The runner
combines it with the solution, compiles with `g++ -std=c++20`, and runs it.
Optional `meta.yaml` can supply missing metadata, for example
`difficulty: Medium` and `topics: [Array, Hash Table]`. Run
`python3 tools/run_tests.py` and `python3 tools/generate_index.py` before a push.
