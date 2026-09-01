# Revision. Same sliding window as the second pass, but the longest update is
# one line: max() replaces the if block, and the length temp goes away.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = set()
        left = 0
        longest = 0

        for right in range(len(s)):

            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            longest = max(longest, right - left + 1)

        return longest
