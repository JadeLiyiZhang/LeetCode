class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        pointer = len(s) - 1
        res = 0
        while s[pointer] == " ":
            pointer -= 1
        
        while s[pointer] != ' ' and pointer >= 0:
            res += 1
            pointer -= 1
        return res