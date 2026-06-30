class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # use 2d dp table
        m = len(text1)
        n = len(text2)
        table = [[0] * n for _ in range(m)]

        # set up edges of table
        for i in range(m):
            table[i][0] = 1 if text1[i] == text2[0] or (i > 0 and table[i - 1][0] == 1) else 0

        for j in range(1, n):
            table[0][j] = 1 if text1[0] == text2[j] or table[0][j - 1] == 1 else 0
        #print(table)
        #now we iterate over i, j space
        for i in range(1, m):
            for j in range(1, n):
                table[i][j] = table[i - 1][j - 1] + 1 if text1[i] == text2[j] else max(table[i - 1][j], table[i][j - 1])
        #print(table)
        return table[m - 1][n - 1]
                            

        
