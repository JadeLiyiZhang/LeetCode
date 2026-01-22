class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        profit = 0
        while sell < len(prices):
            if prices[sell] - prices[buy] < 0:
                buy = sell
            else:
                if prices[sell] - prices[buy] > profit:
                    profit = prices[sell] - prices[buy]
            sell += 1
        return profit