class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = {}
        def recur(n):
            if n < 0:
                return 0
            if n == 0:
                return 1
            if n in dp:
                return dp[n]
            running = 0
            for i in nums:
                running += recur(n - i)
            dp[n] = running
            return running
        # need some DP or caching here
            
        return recur(target)
