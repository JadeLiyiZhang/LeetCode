class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            n = self.unitSquare(n)
            if n == 1:
                return True
            elif n in seen:
                return False
            else:
                seen.add(n)
        

    
    def unitSquare(self, n):
        sum = 0
        while n:
            sum += (n % 10) * (n % 10)
            n //= 10
        return sum