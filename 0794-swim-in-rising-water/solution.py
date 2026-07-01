class Solution(object):
    def swimInWater(self, grid):
        import heapq
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #path with lowest maximum, use dijstrkas with this metric instead of just distance for the edges -- so like edgedict dist is just max of two nodes

        #algo:
        # set up edgedict
        # do dijkstras starting at top left, only need to store distances, not path
        N = len(grid)
        table = {}
        for i in range(N):
            for j in range(N):
                table[(i, j)] = float('inf')
        
        visited = set()

        heap = [[grid[0][0], (0,0)]] #starting at node 0,0 at dist 0
        table[(0,0)] = grid[0][0]
        while heap:
            dist, node = heapq.heappop(heap)
            #print(dist, node)
            i, j = node
            if node in visited:
                continue
            
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < N and 0 <= y < N:
                    neighbor = grid[x][y]
                    newDist = max(neighbor, dist)
                    if newDist < table[(x, y)]:
                        table[(x, y)] = newDist
                        heapq.heappush(heap, [newDist, (x, y)])

            visited.add(node)
        #print(table)
        return table[(N - 1, N - 1)]


        
        
