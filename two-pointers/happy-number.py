class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            res = 0
            while n:
                digit = n % 10
                res += digit * digit
                n //= 10
            return res

        slow = n
        fast = get_next(n)
        
        while fast != 1 and slow != fast:
            slow = get_next(slow)           # 走一步
            fast = get_next(get_next(fast)) # 走两步
            
        return fast == 1
        

