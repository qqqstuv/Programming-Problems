import sys
class Solution:
        
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_buy =  sys.maxsize
        for i in range(len(prices)):
            if prices[i] < min_buy:
                min_buy = prices[i]
            elif prices[i] - min_buy > max_profit:
                max_profit = prices[i] - min_buy
        return max_profit