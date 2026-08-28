class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        max_windows = len(nums) - k + 1
        left = 0
        right = 0 + k - 1
        running_sum = sum(nums[:k])

        highest_sum = running_sum

        for _ in range(max_windows-1):
            running_sum -= nums[left] 
            left += 1
            right += 1
            running_sum += nums[right]

            if running_sum > highest_sum:
                highest_sum = running_sum

        return highest_sum/k


        