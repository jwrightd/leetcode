class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #two choices --> Right, Down

        # right makes it m x n-1
        # down makes it m-1 x n

        # Dp soln?

        #start for i,0 and 0,i, it is i ways. then we can go m,n up until they match
        #table[m, n] is sum of up and left
        
        table = [[0] * n for i in range(m)]
        for i in range(n):
            table[0][i] = 1
        for i in range(m):
            table[i][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                table[i][j] = table[i-1][j] + table[i][j-1]
                
        
        return table[m-1][n-1]



