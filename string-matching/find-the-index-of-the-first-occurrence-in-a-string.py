class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        window = len(needle)
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + window] == needle:
                return i
        return -1