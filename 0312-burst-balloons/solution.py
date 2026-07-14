class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # instead of choosing balloon to do first, what if we choose which one is last
        # then we need to pop left subarray, right subarray, then choice
        padded = [1] + nums + [1]
        n = len(padded)
        dp = [[-1] * n for i in range(n)]

        def dfs(l, r): # l, r --> [l, r]
            if r == l:
                print("here")
                return padded[r - 1] * padded[r] * padded[r + 1]
            if l > r:
                return 0
            for i in range(l, r + 1): # use idx i as thing to pop last/section on
                val = padded[i] * padded[l - 1] * padded[r + 1]
                if dp[l][i - 1] != -1:
                    left = dp[l][i - 1]
                else:
                    left = dfs(l, i - 1)
                    dp[l][i - 1] = left
                if dp[i + 1][r] != -1:
                    right = dp[i + 1][r]
                else:
                    right = dfs(i + 1, r)
                    dp[i + 1][r] = right
                #print(padded[i], right + val + left)
                dp[l][r] = max(dp[l][r], right + val + left)
            return dp[l][r]

        #dfs(1, n - 2)
        return dfs(1, n - 2)
