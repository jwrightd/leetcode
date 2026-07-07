class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        edge = {i:[] for i in range(n)}
        for a, b in edges:
            edge[a].append(b)
            edge[b].append(a)
        visited = set()
        # we can just dfs on every node
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for dst in edge[node]:
                dfs(dst)
            
            return
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count
        

        
