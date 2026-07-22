class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # must use all tickets
        # start at JFK
        # check all connections
        # dfs
        import heapq
        edges = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(edges[src], dst)
        
        # lets try dfs + backtracking 
        #visited = set()
        route = []
        def dfs(node):
            while edges[node]:
                child = heapq.heappop(edges[node])
                #print(child)
                dfs(child)

            route.append(node)
            

        dfs("JFK")
        return route[::-1]

