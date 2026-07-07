class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # maybe we can have a end time nodes in pq
        # for each item, we check if it overlaps with the last end time we pop from heap
        # min meeting rooms is the max number of overlaps at any given time

        # algo
        # let's start by sorting the intervals, or just use heap
        # iterate through, if two intervals are overlapping, we can combine them and push back to heap
        # let's store the number of overlaps they use in the tuple, so we increment when we push back to heap
        # when we pop we check if its bigger than the max num of meeting rooms we currently need

        

        import heapq
        n = len(intervals)
        if n == 1:
            return 1
        
        size = 0 
        
        sortedInts = sorted(intervals)

        heap = [] #end, then start

        for meetingStart, meetingEnd in sortedInts:
            if not heap:
                heapq.heappush(heap, [meetingEnd, meetingStart])
            else:
                soonEnd, soonStart = heap[0]
                if soonEnd <= meetingStart:
                    heapq.heappop(heap)
                    heapq.heappush(heap, [meetingEnd, meetingStart])
                else:
                    heapq.heappush(heap, [meetingEnd, meetingStart])

            size = max(size, len(heap))
        
        return size
            





        
