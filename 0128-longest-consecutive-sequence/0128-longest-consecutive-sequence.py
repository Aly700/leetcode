class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        number_set = set(nums)

        longest_sequence = 0

        for number in number_set:
            if number - 1 not in number_set:
                current = number
                sequence = 1
            
                while current+1 in number_set:
                    current += 1
                    sequence += 1

                if sequence > longest_sequence:
                    longest_sequence = sequence
            

        return longest_sequence








        
        