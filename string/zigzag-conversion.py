class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        direction = 1
        res = [[] for _ in range(numRows)]
        row = 0
        for char in s:
            print(row)
            res[row].append(char)
            if row == 0:
                direction = 1
            if row == numRows - 1:
                direction = -1
            row += direction
        ans = ''
        for _ in res:
            ans += ''.join(_)
        return ans