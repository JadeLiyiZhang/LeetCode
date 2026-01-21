class Solution:
    def countSubstrings(self, s: str) -> int:
        def find_palindrome(left, right, s):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        ans = 0
        for i in range(len(s)):
            ans += find_palindrome(i, i, s)
            ans += find_palindrome(i, i + 1, s)
        return ans
            