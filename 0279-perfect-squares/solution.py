class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # should be greedy
        # or maybe DP
        # ok not greedy
        # if we do greedy then 12 --> 9 1 1 1
        # 13 --> 9 
        dp = {}
        def dfs(num):
            if num == 0:
                return 0
            if num in dp:
                return dp[num]
            smallest = float('inf')
            i = 1
            while num - i ** 2 >= 0:
                res = dfs(num - i ** 2)
                smallest = min(1 + res, smallest)
                i += 1
            dp[num] = smallest
            return smallest
        return dfs(n)
