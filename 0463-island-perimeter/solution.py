class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # each one contributes 4 - number of neighbors of land

        # dfs from 0,0
        M, N = len(grid), len(grid[0])
        visited = set()
        def dfs(i, j):
            if N* i + j in visited:
                return 0
            if grid[i][j] == 0:
                return 0
            visited.add( N* i + j)
            cnt = 0
            adj = 0
            for x,y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if M > x >= 0 and N > y >= 0 and grid[x][y] == 1:
                    cnt += dfs(x, y)
                    adj += 1
            if grid[i][j] == 1:
                val = 4 - adj
                cnt += val

            return cnt
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    return dfs(i, j)
        return 0

# 1 1 1 
# 1 0 0
