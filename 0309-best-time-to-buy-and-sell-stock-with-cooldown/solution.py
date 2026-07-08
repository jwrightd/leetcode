class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # tabular DP i think
        # table[i] would be best profit at i, but we need to memo state as well
        # table[i][j], i is day, j is state (holding, cooling down, not holding)
        # for determining table[i][j]:
        # if j == holding, we just bought or did nothing, so we take max of table[i - 1][holding], table[i - 1][not holding] - prices[i]
        # if j == cooling down, we just sold, so table[i][j] = table[i - 1][holding] + prices[i]
        # if j == not holding, we were just cooling down or not holding
        # so table[i][j] = max(table[i - 1][cool], table[i - 1][not hold])
        # holding = 0, cooldown = 1, not holding = 2
        n = len(prices)
        table = [[0 for i in range(3)] for j in range(n)]
        table[0][0] = -prices[0]
        for i in range(1, n):
            table[i][0] = max(table[i - 1][0], table[i - 1][2] - prices[i])
            table[i][1] = table[i - 1][0] + prices[i]
            table[i][2] = max(table[i - 1][1], table[i - 1][2])
        return max(table[n - 1][1], table[n - 1][2])

        
        
        
        
        #for i in range(n):


        #return table[n - 1]
        
