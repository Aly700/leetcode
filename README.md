# leetcode

My LeetCode solve log. A local script pulls my accepted submissions into
problem directories. The index and `problems.json` are generated from those
directories, and every solution runs its example cases in CI.

<!-- INDEX:BEGIN -->
**Solved:** 21 total | 6 easy | 14 medium | 1 hard

| # | Title | Difficulty | Topics | Language |
| ---: | --- | --- | --- | --- |
| 1 | [Two Sum](0001-two-sum/0001-two-sum.py) | Easy | Array, Hash Table | Python |
| 3 | [Longest Substring Without Repeating Characters](0003-longest-substring-without-repeating-characters/0003-longest-substring-without-repeating-characters.py) | Medium | Hash Table, String, Sliding Window | Python |
| 15 | [3Sum](0015-3sum/0015-3sum.py) | Medium | Array, Two Pointers, Sorting | Python |
| 20 | [Valid Parentheses](0020-valid-parentheses/0020-valid-parentheses.py) | Easy | String, Stack, Bracket Sequences | Python |
| 48 | [Rotate Image](0048-rotate-image/0048-rotate-image.py) | Medium | Array, Math, Matrix | Python |
| 49 | [Group Anagrams](0049-group-anagrams/0049-group-anagrams.py) | Medium | Array, Hash Table, String, Sorting | Python |
| 74 | [Search a 2D Matrix](0074-search-a-2d-matrix/0074-search-a-2d-matrix.py) | Medium | Array, Binary Search, Matrix | Python |
| 84 | [Largest Rectangle in Histogram](0084-largest-rectangle-in-histogram/0084-largest-rectangle-in-histogram.py) | Hard | Array, Stack, Monotonic Stack, Range Minimum/Maximum Query | Python |
| 121 | [Best Time to Buy and Sell Stock](0121-best-time-to-buy-and-sell-stock/0121-best-time-to-buy-and-sell-stock.py) | Easy | Array, Dynamic Programming | Python |
| 125 | [Valid Palindrome](0125-valid-palindrome/0125-valid-palindrome.py) | Easy | Two Pointers, String | Python |
| 128 | [Longest Consecutive Sequence](0128-longest-consecutive-sequence/0128-longest-consecutive-sequence.py) | Medium | Array, Hash Table, Union-Find | Python |
| 155 | [Min Stack](0155-min-stack/0155-min-stack.py) | Medium | Stack, Design | Python |
| 167 | [Two Sum II - Input Array Is Sorted](0167-two-sum-ii-input-array-is-sorted/0167-two-sum-ii-input-array-is-sorted.py) | Medium | Array, Two Pointers, Binary Search | Python |
| 238 | [Product of Array Except Self](0238-product-of-array-except-self/0238-product-of-array-except-self.py) | Medium | Array, Prefix Sum | Python |
| 347 | [Top K Frequent Elements](0347-top-k-frequent-elements/0347-top-k-frequent-elements.py) | Medium | Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect | Python |
| 424 | [Longest Repeating Character Replacement](0424-longest-repeating-character-replacement/0424-longest-repeating-character-replacement.py) | Medium | Hash Table, String, Sliding Window | Python |
| 560 | [Subarray Sum Equals K](0560-subarray-sum-equals-k/0560-subarray-sum-equals-k.py) | Medium | Array, Hash Table, Prefix Sum | Python |
| 566 | [Reshape the Matrix](0566-reshape-the-matrix/0566-reshape-the-matrix.py) | Easy | Array, Matrix, Simulation | Python |
| 643 | [Maximum Average Subarray I](0643-maximum-average-subarray-i/0643-maximum-average-subarray-i.py) | Easy | Array, Sliding Window | Python |
| 739 | [Daily Temperatures](0739-daily-temperatures/0739-daily-temperatures.py) | Medium | Array, Stack, Monotonic Stack | Python |
| 853 | [Car Fleet](0853-car-fleet/0853-car-fleet.py) | Medium | Array, Stack, Sorting, Monotonic Stack | Python |
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
