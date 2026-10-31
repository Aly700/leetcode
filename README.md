# leetcode

My LeetCode solve log. A local script pulls my accepted submissions into
problem directories. The index and `problems.json` are generated from those
directories, and every solution runs its example cases in CI.

<!-- INDEX:BEGIN -->
**Solved:** 35 total | 10 easy | 24 medium | 1 hard

| # | Title | Difficulty | Topics | Language | Solved |
| ---: | --- | --- | --- | --- | --- |
| 1 | [Two Sum](0001-two-sum/0001-two-sum.py) | Easy | Array, Hash Table | Python | 2026-08-27 |
| 3 | [Longest Substring Without Repeating Characters](0003-longest-substring-without-repeating-characters/0003-longest-substring-without-repeating-characters.py) | Medium | Hash Table, String, Sliding Window | Python | 2026-08-17 |
| 11 | [Container With Most Water](0011-container-with-most-water/0011-container-with-most-water.py) | Medium | Array, Two Pointers, Greedy | Python | 2026-09-15 |
| 15 | [3Sum](0015-3sum/0015-3sum.py) | Medium | Array, Two Pointers, Sorting | Python | 2026-08-16 |
| 20 | [Valid Parentheses](0020-valid-parentheses/0020-valid-parentheses.py) | Easy | String, Stack, Bracket Sequences | Python | 2026-08-18 |
| 21 | [Merge Two Sorted Lists](0021-merge-two-sorted-lists/0021-merge-two-sorted-lists.py) | Easy | Linked List, Recursion | Python | 2026-10-29 |
| 33 | [Search in Rotated Sorted Array](0033-search-in-rotated-sorted-array/0033-search-in-rotated-sorted-array.py) | Medium | Array, Binary Search | Python | 2026-10-31 |
| 48 | [Rotate Image](0048-rotate-image/0048-rotate-image.py) | Medium | Array, Math, Matrix | Python | 2026-08-30 |
| 49 | [Group Anagrams](0049-group-anagrams/0049-group-anagrams.py) | Medium | Array, Hash Table, String, Sorting | Python | 2026-08-27 |
| 54 | [Spiral Matrix](0054-spiral-matrix/0054-spiral-matrix.py) | Medium | Array, Matrix, Simulation | Python | 2026-09-15 |
| 73 | [Set Matrix Zeroes](0073-set-matrix-zeroes/0073-set-matrix-zeroes.py) | Medium | Array, Hash Table, Matrix | Python | 2026-09-01 |
| 74 | [Search a 2D Matrix](0074-search-a-2d-matrix/0074-search-a-2d-matrix.py) | Medium | Array, Binary Search, Matrix | Python | 2026-08-25 |
| 84 | [Largest Rectangle in Histogram](0084-largest-rectangle-in-histogram/0084-largest-rectangle-in-histogram.py) | Hard | Array, Stack, Monotonic Stack, Range Minimum/Maximum Query | Python | 2026-08-20 |
| 121 | [Best Time to Buy and Sell Stock](0121-best-time-to-buy-and-sell-stock/0121-best-time-to-buy-and-sell-stock.py) | Easy | Array, Dynamic Programming | Python | 2026-08-17 |
| 125 | [Valid Palindrome](0125-valid-palindrome/0125-valid-palindrome.py) | Easy | Two Pointers, String | Python | 2026-08-26 |
| 128 | [Longest Consecutive Sequence](0128-longest-consecutive-sequence/0128-longest-consecutive-sequence.py) | Medium | Array, Hash Table, Union-Find | Python | 2026-08-14 |
| 153 | [Find Minimum in Rotated Sorted Array](0153-find-minimum-in-rotated-sorted-array/0153-find-minimum-in-rotated-sorted-array.py) | Medium | Array, Binary Search | Python | 2026-10-29 |
| 155 | [Min Stack](0155-min-stack/0155-min-stack.py) | Medium | Stack, Design | Python | 2026-08-18 |
| 167 | [Two Sum II - Input Array Is Sorted](0167-two-sum-ii-input-array-is-sorted/0167-two-sum-ii-input-array-is-sorted.py) | Medium | Array, Two Pointers, Binary Search | Python | 2026-08-16 |
| 200 | [Number of Islands](0200-number-of-islands/0200-number-of-islands.py) | Medium | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix | Python | 2026-08-31 |
| 206 | [Reverse Linked List](0206-reverse-linked-list/0206-reverse-linked-list.py) | Easy | Linked List, Recursion | Python | 2026-10-29 |
| 238 | [Product of Array Except Self](0238-product-of-array-except-self/0238-product-of-array-except-self.py) | Medium | Array, Prefix Sum | Python | 2026-08-13 |
| 347 | [Top K Frequent Elements](0347-top-k-frequent-elements/0347-top-k-frequent-elements.py) | Medium | Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect | Python | 2026-08-13 |
| 424 | [Longest Repeating Character Replacement](0424-longest-repeating-character-replacement/0424-longest-repeating-character-replacement.py) | Medium | Hash Table, String, Sliding Window | Python | 2026-08-25 |
| 496 | [Next Greater Element I](0496-next-greater-element-i/0496-next-greater-element-i.py) | Easy | Array, Hash Table, Stack, Monotonic Stack | Python | 2026-09-01 |
| 560 | [Subarray Sum Equals K](0560-subarray-sum-equals-k/0560-subarray-sum-equals-k.py) | Medium | Array, Hash Table, Prefix Sum | Python | 2026-08-27 |
| 566 | [Reshape the Matrix](0566-reshape-the-matrix/0566-reshape-the-matrix.py) | Easy | Array, Matrix, Simulation | Python | 2026-08-30 |
| 643 | [Maximum Average Subarray I](0643-maximum-average-subarray-i/0643-maximum-average-subarray-i.py) | Easy | Array, Sliding Window | Python | 2026-08-27 |
| 704 | [Binary Search](0704-binary-search/0704-binary-search.py) | Easy | Array, Binary Search | Python | 2026-10-29 |
| 739 | [Daily Temperatures](0739-daily-temperatures/0739-daily-temperatures.py) | Medium | Array, Stack, Monotonic Stack | Python | 2026-08-19 |
| 853 | [Car Fleet](0853-car-fleet/0853-car-fleet.py) | Medium | Array, Stack, Sorting, Monotonic Stack | Python | 2026-08-19 |
| 875 | [Koko Eating Bananas](0875-koko-eating-bananas/0875-koko-eating-bananas.py) | Medium | Array, Binary Search | Python | 2026-10-29 |
| 994 | [Rotting Oranges](0994-rotting-oranges/0994-rotting-oranges.py) | Medium | Array, Breadth-First Search, Matrix | Python | 2026-09-03 |
| 2043 | [Simple Bank System](2043-simple-bank-system/2043-simple-bank-system.py) | Medium | Array, Hash Table, Design, Simulation | Python | 2026-09-20 |
| 3043 | [Find the Length of the Longest Common Prefix](3043-find-the-length-of-the-longest-common-prefix/3043-find-the-length-of-the-longest-common-prefix.py) | Medium | Array, Hash Table, String, Trie | Python | 2026-09-20 |
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
