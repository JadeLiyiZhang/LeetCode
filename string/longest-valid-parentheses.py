class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for index, char in enumerate(s):
            if char == "(":
                stack.append(index)
            else:
                stack.pop()
                if stack:
                    res = max(res, index - stack[-1])
                else:
                    stack.append(index)  
        return res