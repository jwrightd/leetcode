class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # union find or graph + dfs
        # lets do graph and dfs here
        # firt we make the graph

        edges = {}
        for i in range(numCourses):
            edges[i] = []
        for src, dst in prerequisites:
            edges[src].append(dst)
        
        # dfs
        output = []
        visited = set()
        def dfs(node, target):
            if node == target:
                return True
            if node in visited:
                return False
            visited.add(node)

            for neighbor in edges[node]:
                if dfs(neighbor, target):
                    return True
            
            return False

        for src, dst in queries: 
            output.append(dfs(src, dst))
            visited.clear()
        return output


        
