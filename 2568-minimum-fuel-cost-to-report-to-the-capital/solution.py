class Solution(object):
    def minimumFuelCost(self, roads, seats):
        """
        :type roads: List[List[int]]
        :type seats: int
        :rtype: int
        """
        
        # capital -> 0
        # roads are edges
        N = len(roads) + 1
        edges = {}
        for i in range(N):
            edges[i] = []
        for src, dst in roads:
            edges[src].append(dst)
            edges[dst].append(src)
        
        visited = set()
        def dfs(node):
            visited.add(node)
            # post order dfs
            # count total number of people
            # count total number of cars
            # pass both up
            passengerCount = 1
            totalGas = 0
            for nbr in edges[node]:
                if nbr not in visited:
                    gas, people = dfs(nbr)
                    totalGas += gas
                    passengerCount += people
            if node != 0:
                totalGas += ((passengerCount // seats) if passengerCount % seats == 0 else (passengerCount // seats) + 1)
                    
            return totalGas, passengerCount
        
        return dfs(0)[0]
        
