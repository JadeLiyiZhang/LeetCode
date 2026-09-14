class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        res = 0
        for char in s:
            if char == "(":
                stack.append('(')
            # char == ')'
            else:
                if not stack:
                    continue
                stack.pop()
                res += 2
        return res