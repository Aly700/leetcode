class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        running_left = 1
        left_product = []
        running_right = 1
        right_product = [1] * len(nums)
        final_product = []

        for i in range(len(nums)):
            left_product.append(running_left)
            running_left *= nums[i]

        for i in range(len(nums)-1,-1,-1):
            right_product[i] = running_right
            running_right *= nums[i]

        for i in range(len(nums)):
            final_product.append(left_product[i] * right_product[i])

        return final_product

    