class Solution(object):
    def kClosest(self, points, k):
        import heapq
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for x, y in points:
            heapq.heappush(heap, [x**2 + y ** 2, x, y])
        
        output = []
        for i in range(k):
            dist, x, y = heapq.heappop(heap)
            output.append([x, y])
        return output
