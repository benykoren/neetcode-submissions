class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        profit = 0
        for i, val in enumerate(prices):
            profit = max(profit, prices[i] - prices[buy])
            if prices[i] < prices[buy]:
                buy = i
        return profit