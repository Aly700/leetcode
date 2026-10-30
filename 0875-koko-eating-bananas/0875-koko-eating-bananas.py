class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def hours_needed(speed):
            return sum((pile + speed - 1) // speed for pile in piles)

        while left < right:
            middle = (left + right) // 2

            if hours_needed(middle) <= h:
                right = middle
            else:
                left = middle + 1

        return left
