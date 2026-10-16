class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        edgeDict = defaultdict(list)
        for src, dst in edges:
            edgeDict[src].append(dst)
            edgeDict[dst].append(src)
        visited = set()
        def dfs(crt, tgt):
            if crt in visited:
                return False
            if crt == tgt:
                return True
            visited.add(crt)

            for nbr in edgeDict[crt]:
                if dfs(nbr, tgt):
                    return True

            return False
        
        return dfs(source, destination)
        
