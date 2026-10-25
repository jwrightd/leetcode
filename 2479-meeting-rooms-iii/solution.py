class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        # need access to lowest num free room
        # need access to lowest mtg end time
        # just iterate thru mtgs in sorted order
        # array for tracking num times used


        meetings.sort()
        import heapq
        free = []
        used = []

        freq = [0 for _ in range(n)]
        for i in range(n):
            heapq.heappush(free, [i])
        
        for start, end in meetings:
            # move finished meetings to free
            while used and used[0][0] <= start:
                e, l = heapq.heappop(used)
                heapq.heappush(free, [l])
            if free:
                lowest = heapq.heappop(free)[0]
                freq[lowest] += 1
                heapq.heappush(used, [end, lowest])
            else: #wait for used room to finish
                soonest, num = heapq.heappop(used)
                freq[num] += 1
                heapq.heappush(used, [soonest + end - start, num])
        
        idx = -1
        maxFreq = -1
        for i in range(n):
            if freq[i] > maxFreq:
                maxFreq = freq[i]
                idx = i
        return idx



        


