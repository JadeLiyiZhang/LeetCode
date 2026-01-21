class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry, val, res = 0, 0, ''
        for i in range(max(len(a), len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i+1)])
            if i < len(b):
                val += int(b[-(i+1)])
            carry = val // 2
            val = val % 2
            res += str(val)
        if carry:
            res += '1'
        return res[::-1]
