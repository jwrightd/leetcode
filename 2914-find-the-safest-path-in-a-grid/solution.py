class Solution(object):
    def maximumSafenessFactor(self, grid):
        import heapq
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # dijkstra?

        # algo
        # find thieves, precompute manhattan distances for all nodes to thieves
        # edge cost is min of two adj nodes --> or maybe we have to negative values to take neg?
        # do dijkstra

        # optimization - do BFS for manhattan dist
        n = len(grid)
        distToThief = [[-1] * n for _ in range(n)]
        q = []

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    distToThief[i][j] = 0
                    q.append((i, j))

        while q:
            x, y = q.pop(0)
            for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= i < n and 0 <= j < n and distToThief[i][j] == -1:
                    distToThief[i][j] = distToThief[x][y] + 1
                    q.append((i, j))

        
        #now dijkstra

        visited = set()
        table = {}
        for i in range(n):
            for j in range(n):
                table[(i, j)] = float('-inf')
    
        heap = [[-distToThief[0][0], 0,0]] #dist, x, y
        table[(0,0)] = distToThief[0][0]
        while heap:
            dist, x, y = heapq.heappop(heap)

            if (x, y) in visited:
                continue

            if (x, y) == (n - 1, n - 1):
                return -dist
            #if (x, y) == (n - 1, n - 1):
            #    return dist
            
            for i, j in [(x + 1, y), (x-1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= i < n and 0 <= j < n:
                    safe = min(distToThief[i][j], -dist)
                    if safe > table[(i, j)]:
                        #print(i, j, safe)
                        table[(i, j)] = safe
                        heapq.heappush(heap, [-safe, i, j])

            visited.add((x,y))
        #print(table)
        return table[(n - 1, n - 1)]


