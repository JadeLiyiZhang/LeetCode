class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.backtracking(s, 0, [], res)
        return res

    def backtracking(self, s, startIndex, path, res):
        if startIndex == len(s):
            res.append(path[:])
            return

        for i in range(startIndex, len(s)):
            if s[startIndex:i + 1] == s[startIndex:i + 1][::-1]:
                path.append(s[startIndex:i + 1])
                self.backtracking(s, i + 1, path, res)
                path.pop()
