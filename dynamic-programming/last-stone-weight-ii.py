class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum_ = sum(stones)
        target = sum_ // 2
        dp = [0] * (target + 1)
        for stone in stones:
            for j in range(target, stone - 1, -1):
                dp[j] = max(dp[j], dp[j - stone] + stone)
        return sum_ - 2 * dp[target]