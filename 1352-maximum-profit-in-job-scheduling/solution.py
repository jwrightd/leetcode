class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        import bisect
        #dp i = max profit at time i
        # as we process items we eithjehr choose to update dp i
        N = len(profit)
        combined = sorted(zip(startTime, endTime, profit))
        start_times = sorted(startTime)
        visited = set()
        dp = {}
        
        def dfs(i):
            if i >= N:
                return 0
            if i in dp:
                return dp[i]

            
            # either skip or take
            skip = dfs(i + 1)

            # take
            s, e, p = combined[i]
            take = p + dfs(bisect.bisect_left(start_times, e))
            dp[i] = max(skip, take)
            return dp[i]

        
        return dfs(0)
            
        
