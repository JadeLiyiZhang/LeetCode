class Solution:
    def convert(self, s: str, numRows: int) -> str:
        direction = 1
        res = [[] for _ in range(numRows)]
        row = 0
        for char in s:
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