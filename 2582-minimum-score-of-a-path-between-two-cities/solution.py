class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        # dijkstra
        import heapq
        #edges
        edges = {}
        for i in range(1, n + 1):
            edges[i] = []
        
        for src, dst, dist in roads:
            edges[src].append([dst, dist])
            edges[dst].append([src, dist])

        #table
        table = {}
        for i in range(1, n + 1):
            table[i] = float('inf')

        #heap + dijkstra
        # but cant use visited set thing here, just have to prune
        heap = [[float('inf'), 1]] # score, node

        while heap:
            score, node = heapq.heappop(heap)

            for nextNode, dist in edges[node]:
                newDist = min(score, dist)

                if newDist < table[nextNode]:
                    table[nextNode] = newDist
                    heapq.heappush(heap, [newDist, nextNode])

        return table[n]

            



