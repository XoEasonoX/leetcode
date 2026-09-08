class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = prices[0]
        profit = 0
        maxpro = 0
        for i in range(1, len(prices)):
            if prices[i] <= minprice:
                minprice = prices[i]
            else:
                profit = prices[i] - minprice
                if profit >= maxpro:
                    maxpro = profit
        return maxpro