class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #just areafill
        def areafill(grid, i , j):
            if grid[i][j] != 1:
                return 0
            grid[i][j] = -1
            down = areafill(grid, i + 1,  j) if i + 1 < len(grid) else 0
            up = areafill(grid, i - 1, j) if i - 1 >= 0 else 0
            left = areafill(grid, i, j-1) if j-1>= 0 else 0
            right = areafill(grid, i, j + 1) if j + 1 < len(grid[0]) else 0
            return 1 + down + up + left + right
        currMax = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    val = areafill(grid, i, j)
                    if val > currMax:
                        currMax = val
        return currMax

