class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = 0
        prefix_count = {0: 1}
        result = 0

        for number in nums:

            prefix_sum += number

            if (prefix_sum - k) in prefix_count:
                result += prefix_count[prefix_sum-k]


            prefix_count[prefix_sum] = prefix_count.get(prefix_sum,0) + 1


        return result 





        

            

        




        