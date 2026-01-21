class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def dfs(idx, lCount, rCount, sList):
            if idx == len(s):
                if lCount == rCount:
                    if len(self.res) != 0 and self.length < len(sList):
                        self.res = set()
                        self.length = len(sList)
                    if len(self.res) == 0 or self.length == len(sList):
                        self.res.add(''.join(sList))
                return
            c = s[idx]
            if c == '(':
                dfs(idx + 1, lCount, rCount, sList)
                sList.append(c)
                lCount += 1
                dfs(idx + 1, lCount, rCount, sList)
                lCount -= 1
                sList.pop()
            elif c == ')':
                dfs(idx + 1, lCount, rCount, sList)
                if lCount > rCount:
                    sList.append(c)
                    rCount += 1
                    dfs(idx + 1, lCount, rCount, sList)
                    rCount -= 1
                    sList.pop()
            else:
                sList.append(c)
                dfs(idx + 1, lCount, rCount, sList)
                sList.pop()

        self.res = set()
        self.length = 0
        dfs(0, 0, 0, [])
        return list(self.res)