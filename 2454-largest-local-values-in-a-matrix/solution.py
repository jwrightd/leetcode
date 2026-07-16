class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """ # just like sliding grid basically
        # wait no, we just take middle square and chec ksurrounding
        n = len(grid)
        directions = [[1, 0], [1, 1], [0, 1], [-1, 0], [-1, -1], [-1, 1], [0, -1], [1, -1], [0,0]]
        def getMax(i, j):
            tmpMax = float('-inf')
            for x, y in directions:
                if  0 <= i + x < n and 0 <= j + y < n:
                    tmpMax = max(tmpMax, grid[i + x][j + y])
            return tmpMax
        output = []
        for i in range(1, n - 1):
            tmp = []
            for j in range(1, n - 1):
                tmp.append(getMax(i, j))
            output.append(tmp)
        return output

        
