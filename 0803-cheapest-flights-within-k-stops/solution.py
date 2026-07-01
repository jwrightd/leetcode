class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        import heapq
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        #ok we have dijkstras i think
        #but now the variant is that we have k stop max
        #i think we just store the stop in the node as well

        #ok first we do edgeDict
        edges = {i:[] for i in range(n)}

        for origin, end, cost in flights:
            edges[origin].append((end, cost))
        
        #ok now we set up dijkstra 
        maxFlights = k + 1
        visited = set()
        table = {}
        for i in range(n):
            for j in range(maxFlights + 1):
                table[(i, j)] = float('inf')


        heap = [[0, 0, src]] # dist, nth stop, node

        while heap:
            dist, kth, node = heapq.heappop(heap)

            if node == dst:
                return dist

            if (node, kth) in visited or kth >= maxFlights: # to limit to k stops
                continue
            
            for end, cost in edges[node]:
                newDist = cost + dist
                if newDist < table[(end, kth + 1)]:
                    table[(end, kth + 1)] = newDist
                    heapq.heappush(heap, [newDist, kth + 1, end])

            visited.add((node, kth))
        return -1
