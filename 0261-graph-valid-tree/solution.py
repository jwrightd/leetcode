class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1:
            return False
        # do union find
        parent = [i for i in range(n)]
        rank = [0 for i in range(n)]

        def find(x): # w path compression
            if parent[x] == x:
                return x
            else:
                parent[x] = find(parent[x])
                return parent[x]
    
        def union(x, y): # union based on which is shorter
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y: #check if adding edge would make cycle 
                return False
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_y] > rank[root_x]:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
            return True
        
        for a, b in edges: # check for cycle
            if not union(a, b):
                return False 
            
        visited = set()

        edgeDict = {i:[] for i in range(n)}
        for a, b in edges:
            edgeDict[a].append(b)
            edgeDict[b].append(a)
        

        
        return True
                



