# O(1) space. My first pass (kept in the first-pass file) built a cleaned copy
# of the whole string first, which is O(n) extra space. This version two-points
# straight over the original and skips non-alphanumerics in place, so no copy.
# Same O(n) time, but nothing allocated.
class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True

        