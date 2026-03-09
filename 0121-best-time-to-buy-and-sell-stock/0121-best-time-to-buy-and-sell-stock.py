class Solution(object):
    def maxProfit(self, prices):
        l = 1
        low_pri = prices[0]
        profit = 0
        while l < len(prices):
            low_pri = min(prices[l], low_pri)
            profit = max(prices[l] - low_pri, profit)
            l += 1
        return profit

