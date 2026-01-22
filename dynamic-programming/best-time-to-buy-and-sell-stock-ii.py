class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] >= 0:
                profit += (prices[i] - prices[i - 1])

            else:
                res = max(res, profit)
                profit = 0
        res = max(res, profit)
        return res