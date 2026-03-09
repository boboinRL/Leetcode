class Solution(object):
    def maxProfit(self, prices):
        
        low_pri = prices[0]
        profit = 0
        for price in prices:
            if price < low_pri:
                low_pri = price
            if price - low_pri >profit:
                profit = price - low_pri
        return profit

