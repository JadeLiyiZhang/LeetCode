class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        table = {}
        start = 0
        res = 0
        for i, char in enumerate(s):
            if char not in table:
                table[char] = i
            else:
                res = max(res, i - start)
                table[char] = i
                start = i
        return res