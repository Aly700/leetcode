class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        prefix = set()
        longest = 0
        common_prefix = ""

        for number in arr1:

            running = ""

            for char in str(number):

                running += char
                prefix.add(running)
             

        
        for number in arr2:

            running_arr2 = ""

            for char in str(number):

                running_arr2 += char

                if running_arr2 in prefix:

                    longest = max(longest, len(running_arr2))

                

        return longest




        