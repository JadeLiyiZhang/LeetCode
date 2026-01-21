import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        maxSqr = int(math.sqrt(c))
        l, r = 0, maxSqr
        while l <= r:
            ans = l * l + r * r
            if ans > c:
                r -= 1
            elif ans < c:
                l += 1
            else:
                return True
        return False