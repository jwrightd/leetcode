class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # just count 5s and 2s
        # start at 1 and recur with 2 and 5
        #math.log(x, base)
        dp = {}
        fiveCount = 0
        i = 5
        while i <= n:
            
            val = (dp[i//5] + 1 if i//5 in dp else 1)
            dp[i] = val
            fiveCount += val
            i += 5
        return fiveCount
        
