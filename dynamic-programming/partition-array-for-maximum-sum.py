class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        # dp[i]: the max value we can get from 0 - i numbers in the arr after partition
        dp = [0] * (len(arr) + 1)
        
        for i in range(1, len(arr) + 1):
            max_val = 0
            # length: the length of the last partition
            for length in range(1, min(k, i) + 1):
                max_val = max(max_val, arr[i - length])
                dp[i] = max(dp[i], dp[i - length] + max_val * length)
        return dp[len(arr)]