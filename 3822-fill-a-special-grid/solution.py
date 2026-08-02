class Solution(object):
    def specialGrid(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        grid = [[0 for i in range(2 ** n)] for i in range(2 ** n)]
        
        def recur(small, large, x, y, a, b): # top left, bottom right
            #print(small, large)
            if (a - x) == 1 and (b - y) == 1:
                grid[x][y] = small
                return

            else:
                divide = (large - small + 1)//4
                mx = (a + x)//2
                my = (b + y)//2
                recur( small + 3 * divide, large, x, y, mx, my)
                recur( small + 2 * divide, small + 3 * divide - 1, mx, y,a, my)
                recur( small + divide, small + 2 * divide - 1, mx, my, a, b)
                recur( small, small + divide - 1, x, my, mx, b)
        
        recur(0, 2 **(2*n) - 1, 0, 0, 2 ** n, 2 ** n)
        return grid
                
        
