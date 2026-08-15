class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        # dijkstras
        import heapq
        table = {}
        m = len(heights)
        n = len(heights[0])
        heap = [[0, 0, 0]] # effort, i, j
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        table[(0,0)] = 0
        while heap:
            effort, i, j = heapq.heappop(heap)
            for x, y in directions:
                if 0 <= i + x < m and 0 <= j + y < n:
                    newEffort = max(abs(heights[i][j] - heights[i + x][j + y]), effort)
                    if (i + x, j + y) not in table or table[(i + x, j + y)] > newEffort:
                        table[(i + x, j + y)] = newEffort
                        heapq.heappush(heap, [newEffort, i + x, j + y ])



        return table[(m - 1, n - 1)]

        
