class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        costs = [0] + costs
        dp = [float('inf') for i in range(n + 1)]
        dp[0] = 0
        for start in range(n):
            for end in range(1, 4):
                if start + end > n:
                    continue
                idx = start + end
                jumpCost = costs[idx] + (end) ** 2
                potentialCost = dp[start] + jumpCost
                if potentialCost < dp[idx]:
                    dp[idx] = potentialCost



        return dp[-1]
