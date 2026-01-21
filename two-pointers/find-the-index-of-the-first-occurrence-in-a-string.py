class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        while left <= len(haystack) - len(needle):
            if haystack[left: left + len(needle)] == needle:
                return left
            left += 1
        return -1