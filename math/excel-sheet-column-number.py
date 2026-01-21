class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        list_char = list(columnTitle)[::-1]
        for i in range(len(list_char)):
            num = (ord(list_char[i]) - ord('A')) + 1
            res += num * 26 ** i
        
        return res