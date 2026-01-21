class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [0] * (K + 1)
        m = 0
        while dp[K] < N:
            m += 1
            for eggs in range(K, 0, -1):
                dp[eggs] = dp[eggs] + dp[eggs - 1] + 1
        return m