class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        # areafill sums, then count

        visited = set()
        M, N = len(grid), len(grid[0])

        cnt = 0

        def dfs(i, j):
            if (i, j) in visited:
                return 0 
            if grid[i][j] == 0:
                return 0
            visited.add((i, j))
            tot = grid[i][j]
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < M and 0 <= y < N:
                    tot += dfs(x, y)


            return tot

        for i in range(M):
            for j in range(N):
                tot = dfs(i, j)
                if tot % k == 0 and tot != 0:
                    cnt += 1


        return cnt
