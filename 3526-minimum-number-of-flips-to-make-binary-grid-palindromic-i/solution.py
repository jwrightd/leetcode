class Solution(object):
    def minFlips(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def checkRows():
            count = 0
            for row in grid:
                for i in range(len(row)//2):
                    if row[i] != row[len(row) - i - 1]:
                        count += 1
            return count
        def checkCols():
            count = 0
            M = len(grid)
            N = len(grid[0])
            for i in range(N):
                col = [grid[m][i] for m in range(M)]
                for i in range(len(col)//2):
                    if col[i] != col[len(col) - i - 1]:
                        count += 1
            return count
        return min(checkRows(), checkCols())
        
