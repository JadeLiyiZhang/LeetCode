from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        n = len(triangle)
        # 1) dp 初始为最后一行（要拷贝一份）
        dp = triangle[-1][:]

        # 2) 从倒数第二行开始往上推
        for i in range(n - 2, -1, -1):
            # 这一行有 i+1 个元素，左到右更新即可
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
                # dp[j] 用到的是“下一行”的 dp[j], dp[j+1]
                # 左到右更新不会覆盖将要用到的 dp[j+1]
        return dp[0]
