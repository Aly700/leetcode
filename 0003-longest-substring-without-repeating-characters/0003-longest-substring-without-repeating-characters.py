class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = set()
        left = 0
        right = 0
        longest = 0

        for right in range(len(s)):

            if s[right] not in char_set:
                char_set.add(s[right])
                length = right - left + 1
                right += 1


                if length > longest:
                    longest = length

            else:

                while s[right] in char_set:
                    char_set.remove(s[left])
                    left += 1
                
                char_set.add(s[right])
                right +=1

        return longest

        
        
        