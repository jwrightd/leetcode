class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        #dynamic programming
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(1, n + 1):
            dp[0][i] = i
        for i, char1 in enumerate(word1, 1):
            dp[i][0] = i
            for j, char2 in enumerate(word2, 1):
                if char1 == char2:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
        return dp[m][n]
        
