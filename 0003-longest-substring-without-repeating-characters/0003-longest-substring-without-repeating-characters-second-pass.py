# Revision. My first pass (kept in the first-pass file) advanced `right` by hand
# even though the for loop already controls it, so those writes were dead code and
# the branch was duplicated. Same O(n) sliding window either way, this version is
# just simpler and does less redundant work per step.
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
            length = right - left + 1

            if length > longest:
                longest = length

        return longest
        
        