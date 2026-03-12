class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = {}
        length = 0
        res = 0
        for i, char in enumerate(s):
            if char not in table:
                table[char] = i
                length += 1
            else:
                res = max(res, i - table[char])
                length = 1
                table[char] = i
        return max(length, res)