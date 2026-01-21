class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        num_sum = sum(nums)
        dp = [0] * 10001
        if num_sum % 2 == 1:
            return False
        target = num_sum // 2
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = max(dp[j], dp[j - num] + num)
        return dp[target] == target