class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency = {}
        
        for number in nums:
            frequency[number] = frequency.get(number,0) + 1
        
        buckets = [[] for _ in range(len(nums)+1)]

        for number, count in frequency.items():
            buckets[count].append(number)

        result = []

        for i in range(len(buckets)-1,0,-1):
            for number in buckets[i]:
                result.append(number)

                if len(result) == k:
                    return result

        return result