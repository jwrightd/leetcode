class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        # just dp + dfs
        # table i j is max length, when we check children
        m = len(matrix)
        n = len(matrix[0])

        table = [[-1 for i in range(n)] for i in range(m)] # path init 1


        def dfs(i, j):
            highest = 1
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    if table[x][y] == -1:
                        res = dfs(x, y)
                        table[x][y] = res
                    else:
                        res = table[x][y]
                    highest = max(res + 1, highest)

            return highest

        ret = 1
        for i in range(m):
            for j in range(n):
                    ret = max(dfs(i, j), ret)
        return ret


        
