class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # ohhh, this is actually a graph problem
        # we want to see what connected components there are
        # so we want to do edge dict
        # and then dfs
       # pairs.sort()
        visited = set()
        edges = defaultdict(list)
        for a, b in pairs:
            edges[a].append(b)
            edges[b].append(a)
        n = len(s)
        output = [i for i in s]
        component = []
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            component.append(node)
            for edge in edges[node]:
                dfs(edge)
        
        for i in edges:
            dfs(i)

            sortedComp = sorted(component)
            res = sorted([s[i] for i in sortedComp])

            for idx, val in enumerate(sortedComp):
                output[val] = res[idx]
            component = []
        for i in edges:
            if i not in visited:
                output[i] = s[i]
        return "".join(output)
            
        
