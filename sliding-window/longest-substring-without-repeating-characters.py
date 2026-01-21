class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        right = 0
        table = {}
        while right < len(s):
            if s[right] in table and table[s[right]] >= left:
                left = table[s[right]] + 1
            longest = max(longest, (right - left) + 1)
            table[s[right]] = right
            right += 1
        return longest
