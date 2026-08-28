class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        number_map = {}

        for i,number in enumerate(nums):

            complement = target - number

            if complement in number_map:

                return[number_map[complement] , i]

            number_map[number] = i

        return []

        







        

        