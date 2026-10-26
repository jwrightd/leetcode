class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # number of contiguous islands, cannot touch border

        num_islands = 0
        M, N = len(grid), len(grid[0])
        visited = set()
        def dfs(i, j):
            #if (i, j) in visited:
            #    return 1
            if i == 0 or i == M - 1 or j == 0 or j == N - 1:
                return 0
            visited.add((i, j))
            res = 1
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < M and 0 <= y < N and grid[x][y] == 0 and (x, y) not in visited:
                    res &= dfs(x, y)


            return res

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0 and (i, j) not in visited:
                    num_islands += dfs(i, j)
        return num_islands

        
