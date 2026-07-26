class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        tgt = n - 1
        import heapq
        outgoing = defaultdict(list)
        incoming = defaultdict(list)
        weights = {}
        for u, v, w in edges:
            weights[(u, v)] = w
            incoming[v].append(u)
            outgoing[u].append(v)
        table = {}
        for u, v, w in edges:
            table[u] = table[v] = float('inf')
        table[0] = 0
        heap = [[0, 0]] # dist, start node
        while heap:
            dist, node = heapq.heappop(heap)
            for neigh in outgoing[node]:
                newDist = dist + weights[(node, neigh)]
                if newDist < table[neigh]:
                    heapq.heappush(heap, [newDist, neigh])
                    table[neigh] = newDist
            for neigh in incoming[node]:
                if (neigh, node) in weights and dist + 2 * weights[(neigh, node)] < table[neigh]:
                    heapq.heappush(heap, [dist + 2 * weights[(neigh, node)], neigh])
                    table[neigh] = dist+ 2 * weights[(neigh, node)]
        return table[tgt] if tgt in table and table[tgt] != float('inf')  else -1      
