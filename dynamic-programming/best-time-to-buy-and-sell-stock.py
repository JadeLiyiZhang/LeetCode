class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for sell in prices:
            if sell - buy < 0:
                buy = sell
            else:
                profit = max(profit, sell - buy)
        return profit