class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        greater = {}

        for number in nums2:

            while stack and number > stack[-1]:
                greater[stack.pop()] = number

            stack.append(number)

        return [greater.get(number,-1) for number in nums1]

    

            












        