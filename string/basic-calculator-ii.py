class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        prev_sign = '+'
        for i in range(len(s) + 1):
            char = s[i] if i < len(s) else '\0'

            if char.isdigit():
                num = 10 * num + int(char)

            if not char.isdigit() and char != ' ' or i == len(s):
                if prev_sign == "+":
                    stack.append(num)
                if prev_sign == "-":
                    stack.append(-num)
                if prev_sign == "*":
                    stack.append(stack.pop() * num)
                if prev_sign == "/":
                    stack.append(int(stack.pop() / num))
                
                prev_sign = char
                num = 0
        return sum(stack)