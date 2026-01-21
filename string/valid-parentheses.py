class Solution:
    def isValid(self, s: str) -> bool:
        table = {'(': ")", "{": "}", "[": "]"}
        stack = []
        for par in s:
            if par in "({[":
                stack.append(par)
            else:
                if not stack:
                    return False
                pair = stack.pop()
                if par != table[pair]:
                    return False
        return True if not stack else False