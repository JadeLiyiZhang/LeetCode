class Solution:
    def isHappy(self, n: int) -> bool:
        def unit_square_sum(n):
            res = 0
            while n:
                res += ((n % 10) * (n % 10))
                n //= 10
            return res
        seen = set()
        while True:
            temp = unit_square_sum(n)
            if temp in seen:
                return False
            elif temp == 1:
                return True
            else:
                seen.add(temp)
                n = temp

        

