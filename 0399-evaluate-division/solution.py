class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # graph problem I think
        # equation with weighst
        # traverse graph and multiply edges
        # if src or dst is not in edges then return -1
        # if src == dst, return 1
        # probably just ccreate graph, then DFS over it
        # if a/b = 2, a = 2b
        # first make graph
        # graph is bidirectional but with diff weights
        edges = {}
        for idx, val in enumerate(equations):
            numerator, denominator = val[0], val[1]
            ans = values[idx]
            if numerator not in edges:
                edges[numerator] = []
            if denominator not in edges:
                edges[denominator] = []
            edges[numerator].append([denominator, ans])
            edges[denominator].append([numerator, 1/ans])
        
        # now dfs

        output = []
        visited = set()

        def dfs(node, target):
            if node == target:
                return 1
            if node in visited:
                return 0
            visited.add(node)
            for neighbor in edges[node]:
                neigh, mult = neighbor
                res = dfs(neigh, target)
                if res:
                    return res * mult
            return 0
        
        for num, den in queries:
            if num in edges and den in edges:
                res = dfs(num, den)
                if res == 0:
                    output.append(-1)
                else:
                    output.append(res)
                visited.clear()
            else:
                output.append((-1))
        return output
