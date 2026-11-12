class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        chosen = []

        def walk(i):
            if i == len(nums):
                result.append(chosen[:])
                return

            chosen.append(nums[i])
            walk(i + 1)
            chosen.pop()
            walk(i + 1)

        walk(0)

        return result
