class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        par = [i for i in range(n + 1)]

        def find(i):
            if par[i] != i:
                return find(par[i])
            return i
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            par[p1] = p2
            if p1 == p2:
                return True
            return False
        
        for x,y in edges:
            res = union(x, y)
            if res:
                return [x, y]


