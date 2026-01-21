class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        res = [[] for _ in range(numRows)]
        idx, d = 0, 1
        
        for char in s:
            res[idx].append(char)
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d
        
        for _ in range(numRows):
            res[_] = ''.join(res[_])
        res = ''.join(res)
        return res