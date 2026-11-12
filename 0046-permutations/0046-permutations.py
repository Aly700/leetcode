class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        chosen = []
        used = [False] * len(nums)

        def walk():
            if len(chosen) == len(nums):
                result.append(chosen[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                chosen.append(nums[i])
                walk()
                chosen.pop()
                used[i] = False

        walk()

        return result
