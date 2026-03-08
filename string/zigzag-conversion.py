class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for i in range(numRows)]
        direction = 1
        row = 0
        for char in s:
            if row == numRows - 1:
                direction = -1
            elif row == 0:
                direction = 1
            res[row].append(char)
            row += direction
        ans = ''
        for line in res:
            ans += ''.join(line)
        return ans