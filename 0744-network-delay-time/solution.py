class Solution(object):
    def networkDelayTime(self, times, n, k):
        import heapq
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        edges = {i:[] for i in range(1, n + 1)}
        for u, v, w in times:
            edges[u].append((v,w))

        visited = set()

        table = {}
        for node in range(1, n + 1):
            table[node] = float('inf') #distance, prev node

        table[k] = 0 # we start with this one
        
        heap = []
        heapq.heappush(heap, (0, k))# (0, k) is (distance, node)
        while heap:
            dist, node = heapq.heappop(heap)
            if node in visited:
                continue
            #iterate thru neighbors
            for neighbor, cost in edges[node]:
                if neighbor not in visited:
                    newDist = cost + dist
                    if newDist < table[neighbor]:
                        table[neighbor] = newDist
                        heapq.heappush(heap, (newDist, neighbor))
            visited.add(node)

        biggest = float('-inf')
        for i in range(1, n + 1):
            if table[i] == float('inf'):
                return -1
            biggest = max(biggest, table[i])
        return biggest
        

        





        
