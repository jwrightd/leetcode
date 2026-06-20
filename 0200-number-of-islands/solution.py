class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #areafill, if we get a 1 we add to global counter
        m = len(grid)
        n = len(grid[0])
        num = 0

        def areaFill(i, j):
            if i < 0 or i == m or j < 0 or j == n or grid[i][j] != "1":
                return
            grid[i][j] = "X"
            areaFill(i + 1, j)
            areaFill(i - 1, j)
            areaFill(i, j - 1)
            areaFill(i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    num += 1
                    areaFill(i, j)
   
        return num

