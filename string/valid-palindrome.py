class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = s.lower()
        left, right = 0, len(s) - 1
        def isNonAlpha(char):
            return not (char.isdigit() or char.isalpha())
        while left < right:
            while left < right and isNonAlpha(s[left]):
                left += 1
            while left < right and isNonAlpha(s[right]):
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True