class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        point1 = len(num1) - 1
        point2 = len(num2) - 1
        res = []
        carry = 0
        while point1 >= 0 or point2 >= 0:
            temp1 = int(num1[point1]) if point1 >= 0 else 0
            temp2 = int(num2[point2]) if point2 >= 0 else 0
            sum = (temp1 + temp2 + carry) % 10
            carry = (temp1 + temp2 + carry) // 10
            res.append(str(sum))
            point1 -= 1
            point2 -= 1
        if carry:
            res.append(str(carry))
        return ''.join(res)[::-1]