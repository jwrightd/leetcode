class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #is this graph theory, you make the edges and check for cycles?
        #directed graph, use visit set to detect cycles
        # do dfs

        #first, we need edges map

        edgeMap = dict()
        for i in range(numCourses):
            edgeMap[i] = []
        for course, prereq in prerequisites:
            edgeMap[course].append(prereq)
        

        visited = set()
        #now we do dfs
        def dfs(course):
            #print(course)
            if edgeMap[course] == []:
                return True
            if course in visited:
                return False
            visited.add(course)
            for c in edgeMap[course]:
                if not dfs(c):
                    return False
            visited.remove(course)
            edgeMap[course] = []
            return True
        
        for i in range(numCourses):
            res = dfs(i)
            #print(i, res)
            if not res:
                return False
        
        return True
                
            
        
            


