class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # dp[i][j]: s[i:j + 1] is palindrome or not
        dp = [[False] * n for _ in range(n)]
        max_len = 1
        best_l, best_r = 0, 0
        for i in range(n):
            dp[i][i] = True
        for _len in range(2, n + 1):
            for l in range(n - _len + 1):
                r = l + _len - 1
                if s[l] == s[r]:
                    if _len > 3:
                        dp[l][r] = dp[l + 1][r - 1]
                    else:
                        dp[l][r] = True

                if dp[l][r] and r - l + 1 > max_len:
                    max_len = r - l + 1
                    best_l, best_r = l, r
        return s[best_l : best_r + 1]
                    