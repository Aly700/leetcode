class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        left = 0
        max_frequency = 0
        longest = 0

        for right in range(len(s)):

            count[s[right]] = count.get(s[right], 0) + 1
            max_frequency = max(max_frequency, count[s[right]])

            while (right - left + 1) - max_frequency > k:
                
                count[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest




        