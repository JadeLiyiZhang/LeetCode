class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            speed = left + (right - left) // 2
            count = 0
            for pile in piles:
                count += (pile + speed - 1) // speed
            if count > h:
                left = speed + 1
            if count <= h:
                right = speed
        return left