class Solution(object):
    def wallsAndGates(self, rooms):
        from collections import deque
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        # is this the BFS thing? no its not
        # wait we do BFS for sure from the gates
        # but what's the optimization?
        INF = 2147483647
        queue = deque()
        m = len(rooms)
        n = len(rooms[0])
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append([i, j])
        visited = set()
        while queue:
            i, j = queue.popleft()

            if (i, j) in visited:
                continue
            
            visited.add((i, j))
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and rooms[x][y] == INF:
                    rooms[x][y] = rooms[i][j] + 1
                    queue.append([x, y])
        




        
