import heapq
class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        #graph problem
        # greedy algorithm, kruskal's

        #first we set up adj list
        n = len(points)

        adjList = {i:[] for i in range(n)} # i to [distance, node]

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                adjList[i].append([distance, j])
                adjList[j].append([distance, i])
        
        #Prim's now
        cost = 0
        visited = set()
        minHeap = []
        minHeap.append([0,0])

        while len(visited) < n:
            node = heapq.heappop(minHeap)
            c, idx = node
            if idx not in visited:
                cost += c
                visited.add(idx)
                for neighborCost, neighbor in adjList[idx]:
                    if neighbor not in visited:
                        heapq.heappush(minHeap, [neighborCost, neighbor])
        return cost
            


        
