class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        n = len(prices)
        idx = 1
        while idx < n:
            if prices[idx] > prices[idx - 1]:
                profit += (prices[idx] - prices[idx - 1])
            idx += 1
        return profit
        
