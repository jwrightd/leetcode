class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        depth = len(triangle)
        width = len(triangle[-1])
        dp = {}
        dp[(0,0)] = triangle[0][0]

        def dfs(i, j):
            #if (i, j) in dp:
            #    return dp[(i, j)]
            for x, y in [(i + 1, j), (i + 1, j + 1)]:
                if x < depth and y < width:
                    if (x, y) not in dp or dp[(i, j)] + triangle[x][y] < dp[(x, y)]:
                        dp[(x, y)] = dp[(i, j)] + triangle[x][y]
                        dfs(x, y)



        dfs(0,0)
        lowest = float('inf')
        for i in range(width):
            lowest = min(lowest, dp[(depth - 1, i)])
        return lowest

