class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1
        def isNonAlpha(char):
            if char.isdigit():
                return False
            elif char.isalpha():
                return False
            return True
        while left < right:
            while isNonAlpha(s[left]):
                left += 1
            while isNonAlpha(s[right]):
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True