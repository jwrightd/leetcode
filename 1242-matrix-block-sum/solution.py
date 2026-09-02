class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # 1 2 3 
        # 4 5 6
        # 7 8 9
        # prefix sum matrix
        # subtract stuff out
        M = len(mat)
        N = len(mat[0])
        dp = [[0 for i in range(N + 1)] for j in range(M + 1)]
        #for i in range(1, N):
        #    dp[0][i] = mat[0][i] + dp[0][i - 1]
        #for j in range(1, M):
        #    dp[j][0] = mat[j][0] + dp[j - 1][0]
        
        for i in range(M):
            for j in range(N):
                dp[i + 1][j + 1] = mat[i][j] + dp[i][j + 1] + dp[i + 1][j] - dp[i][j]

        def getVal(r, c, k):
            minR, maxR = max(0, r - k), min(M - 1, r + k) + 1
            minC, maxC = max(0, c - k), min(N - 1, c + k) + 1
            return dp[maxR][maxC] + dp[minR][minC] - dp[maxR][minC] - dp[minR][maxC]
        output = [[0 for i in range(N)] for j in range(M)]
        for i in range(M):
            for j in range(N):
                output[i][j] = getVal(i, j, k)

        return output


