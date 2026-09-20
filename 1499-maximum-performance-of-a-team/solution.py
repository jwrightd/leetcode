class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        # perf = sum speed * min efficiency
        # maybe we select our least efficient engineer first
        # so loop thru all engineers, considering each as the minimum
        # then we have min heap of size k of the best k speeds
        # sum andmuklt by min eff, track global max
        N = len(efficiency)
        engineers = [[efficiency[i], speed[i]] for i in range(N)]
        engineers.sort(reverse=True)

        import heapq
        heap = [] # size k
        totalSpeed = 0

        globalMax = float('-inf')

        for i in range(N):
            eff, spd = engineers[i]
            heapq.heappush(heap, spd)
            totalSpeed += spd
            if len(heap) > k:
                totalSpeed -= heapq.heappop(heap)
            globalMax = max(globalMax, eff * totalSpeed)
        return globalMax % (10 ** 9 + 7)



        
