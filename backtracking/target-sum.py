class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_ = sum(nums)
        if abs(target) > sum_:
            return 0
        if (sum_ - abs(target)) % 2 != 0:
            return 0
        val = (target + sum_) // 2
        dp = [0] * (val + 1)
        dp[0] = 1
        for num in nums:
            for j in range(val, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[val]