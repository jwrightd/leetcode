class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        #dp
        clen = len(cost)
        table = [0 for i in range(clen)]

        table[0] = cost[0]
        table[1] = cost[1]

        for i in range(2, clen):
            table[i] = cost[i] + min(table[i - 1], table[i - 2])


        return min(table[clen - 1], table[clen - 2])

        


        
