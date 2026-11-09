class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = defaultdict(int)
        cols = defaultdict(int)
        cnt = 0
        tot = 0
        M, N = len(grid), len(grid[0])
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    tot += 1
                    rows[i] += 1
                    cols[j] += 1
        
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1 and cols[j] == rows[i] == 1:
                    cnt += 1

        return tot - cnt

