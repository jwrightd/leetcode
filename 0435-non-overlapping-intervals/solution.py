class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 1:
            return 0
        count = 0
        import heapq

        heapq.heapify(intervals)
        while len(intervals) >= 2:
            s1, e1 = heapq.heappop(intervals)
            s2, e2 = heapq.heappop(intervals)

            if e1 > s2: # overlap
                count += 1
                if e2 < e1:
                    heapq.heappush(intervals, [s2, e2])
                else:
                    heapq.heappush(intervals, [s1, e1])
            else:
                heapq.heappush(intervals, [s2, e2])
        return count
        #algo
        # let's do greedy!
        # sort intervals
        # process them, if first two intervals overlap, take smaller end element
        # track

        #so we pop two, 
        
