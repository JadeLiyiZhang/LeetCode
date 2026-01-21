class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [0] * len(grid[0])
        dp[0] = grid[0][0]
        for i in range(1, len(grid[0])):
            dp[i] = grid[0][i] + dp[i - 1]
        for j in range(1, len(grid)):
            dp[0] = dp[0] + grid[j][0]
            for i in range(1, len(grid[0])):
                dp[i] = min(dp[i], dp[i - 1]) + grid[j][i]
        return dp[-1]