class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        # number of things

        edges = {}
        N = len(isConnected)
        for i in range(N):
            edges[i] = []
        
        for i in range(N):
            for j in range(i + 1, N):
                if i == j or isConnected[i][j] == 0:
                    continue
                edges[i].append(j)
                edges[j].append(i)
        

        count = 0
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nbr in edges[node]:
                dfs(nbr)
        for i in range(N):
            if i in visited:
                continue
            count += 1
            dfs(i)
        return count
