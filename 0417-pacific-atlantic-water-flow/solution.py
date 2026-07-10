class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        # dfs + memo

        # okay we can do 2d DP for call at (i, j)
        # why dont we just check what hits atlantic, what hits pacific, and then intersect
        pacific = set()
        atlantic = set()

        m = len(heights)
        n = len(heights[0])


        def dfs(i, j, visited):
            visited.add((i, j))
            # recur on smaller nums

            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and heights[x][y] >= heights[i][j]:
                   dfs(x, y, visited)

        
        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n - 1, atlantic)
        
        for j in range(n):
            dfs(0, j, pacific)
            dfs(m - 1, j, atlantic)

        output = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    output.append([i, j])
        return output
