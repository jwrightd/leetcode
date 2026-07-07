class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n = len(intervals)
        if n == 1:
            return 1
        import heapq
        removed = 0
        heap = []
        for i in intervals:
            heapq.heappush(heap, i)
        
        while len(heap) >= 2:
            s1, e1 = heapq.heappop(heap)
            s2, e2 = heapq.heappop(heap)
            if s1 <= s2 and e1 >= e2:
                heapq.heappush(heap, [s1, e1])
                removed += 1
            elif s2 <= s1 and e2 >= e1:
                heapq.heappush(heap, [s2, e2])
                removed += 1
            else:
                heapq.heappush(heap, [s2, e2])
        return n - removed


        
