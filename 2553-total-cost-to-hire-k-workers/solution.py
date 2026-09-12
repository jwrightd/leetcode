class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        import heapq

        left = []
        right = []
        N = len(costs)
        
        l, r = 0, N - 1

        total = 0

        while l < candidates and l < N:
            heapq.heappush(left, [costs[l], l])
            l += 1
        while r >= l and len(right) < candidates:
            heapq.heappush(right, [costs[r], r])
            r -= 1
        
        for _ in range(k):
            # 3 cases - both have el, r has el, l has el

            if len(right) > 0 and len(left) > 0:
                smallestLeft, lIdx = left[0]
                smallestRight, rIdx = right[0]
                if smallestLeft <= smallestRight:
                    heapq.heappop(left)
                    total += smallestLeft
                    if l <= r and l >= 0:
                        heapq.heappush(left, [costs[l], l])
                        l += 1
                else:
                    total += smallestRight
                    heapq.heappop(right)
                    if l <= r and r < N:
                        heapq.heappush(right, [costs[r], r])
                        r -= 1
            elif len(right) > 0:
                smallestRight, rIdx = heapq.heappop(right)
                total += smallestRight
                if l <= r and r < N:
                    heapq.heappush(right, [costs[r], r])
                    r -= 1
            elif len(left) > 0:
                smallestLeft, lIdx = heapq.heappop(left)
                total += smallestLeft
                if l <= r and l >= 0:
                    heapq.heappush(left, [costs[l], l])
                    l += 1
        return total



                


        
