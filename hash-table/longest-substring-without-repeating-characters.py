class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = {}
        start = 0
        res = 0

        for i, char in enumerate(s):
            if char in table and table[char] >= start:
                start = table[char] + 1

            table[char] = i
            res = max(res, i - start + 1)

        return res