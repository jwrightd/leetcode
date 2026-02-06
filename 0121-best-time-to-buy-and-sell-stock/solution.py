class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices) - 1
        maxProfit = prices[n] - prices[0]
        minPrice = prices[0]
        for p in prices[1:]:
            maxProfit = max(maxProfit, p - minPrice)
            minPrice = min(minPrice, p)
        return maxProfit if maxProfit > 0 else 0
