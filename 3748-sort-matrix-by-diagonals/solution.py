class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        # so we take each diagonal, sort the numbers, update the nnums
        m = len(grid)
        n = len(grid[0])

        def getDiag(i, j):
            output = []
            while i < m and j < n:
                output.append([i, j])
                i += 1
                j += 1
            return output
        
        for i in range(1, n): # blue
            diag = getDiag(0, i)
            nums = [grid[i][j] for i, j in diag]
            nums.sort()
            for idx, val in enumerate(nums):
                ix, jx = diag[idx]
                grid[ix][jx] = val


        for i in range(m): # blue
            diag = getDiag(i, 0)
            nums = [grid[i][j] for i, j in diag]
            nums.sort(reverse = True)
            for idx, val in enumerate(nums):
                ix, jx = diag[idx]
                grid[ix][jx] = val
        return grid
        


