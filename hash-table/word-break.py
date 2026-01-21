class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        set_dict = set(wordDict)
        max_len = 0
        for word in wordDict:
            if len(word) > max_len:
                max_len = len(word)

        for i in range(1, len(s) + 1):
            for j in range(max(0, i - max_len), i + 1):
                if dp[j] and s[j:i] in set_dict:
                    dp[i] = True
        return dp[len(s)]