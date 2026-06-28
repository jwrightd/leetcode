class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        #first, dir graph
        edges = {i:[] for i in range(numCourses)} #course:pre
        for course, pr in prerequisites:
            edges[course].append(pr)
        
        visited = set() # detect cycles
        processed = set()
        order = []
        def dfs(course): # backtracking
            if course in visited:
                return False
            if course in processed:
                return True
            visited.add(course)
            for c in edges[course]:
                if not dfs(c):
                    return False
            order.append(course)
            visited.remove(course)
            processed.add(course)
            return True

        for i in range(numCourses): # also fix this
            if i not in processed:
                if not dfs(i):
                    return [] # means it is not possible
        return order

        
