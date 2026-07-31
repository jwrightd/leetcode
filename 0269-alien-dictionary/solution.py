class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # make graph
        # post order dfs
        # return

        # first, we make the graph
        # directed graph, so a nodes neighbors are all greater than it
        def getDiff(a, b):
            i = 0
            n, m = len(a), len(b)
            while i < min(n, m):
                if a[i] == b[i]:
                    i += 1
                else:
                    return i
            return -1 if len(a) > len(b) else i

        edges = defaultdict(list)
        N = len(words)
        i = 0
        while i < N - 1:
            a = words[i]
            b = words[i + 1]
            if a == b:
                i += 1
                continue
            firstDiff = getDiff(a, b)
            if firstDiff == -1:
                return ""
            elif firstDiff >= len(a):
                i += 1
                continue
            edges[a[firstDiff]].append(b[firstDiff])
            i += 1
        #print(edges)
        visited = set()
        processed = set()
        output = []
        def postOrder(node):
            if node in processed:
                return True
            if node in visited:
                return False
            
            
            visited.add(node)
            
            for neigh in edges[node]:
                if not postOrder(neigh):
                    return False
            
            processed.add(node)
            output.append(node)
            return True
        chars = set("".join(words))
        for node in chars:
            if node not in processed:
                if not postOrder(node):
                    return ""

        return "".join(output[::-1])



