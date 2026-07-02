class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        import heapq
        m = len(grid)
        n = len(grid[0])
        #dijkstras but we index health and node
        visited = set()
        table = {}
        for i in range(m):
            for j in range(n):
                table[(i, j)] = float('inf')
        
        heap = [[-(health - grid[0][0]), 0,0]] # dist
        table[(0,0)] = health - grid[0][0]

        while heap:
            negHealth, x, y = heapq.heappop(heap)
            health = -negHealth
            if (x, y) in visited or -negHealth < 1:
                continue
            
            if (x, y) == (m - 1, n - 1):
                return True
            
            for i, j in [(x + 1, y), (x-1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= i < m and 0 <= j < n:
                    newDist = health if grid[i][j] == 0 else health - 1
                    if newDist < table[(i, j)]:
                        table[(i, j)] = newDist
                        heapq.heappush(heap, [-newDist, i, j])

            visited.add((x, y))

        return False
        
        
