class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        import heapq
        N = len(nums)
        table = {}
        
        for idx in range(N):
            table[idx] = float('-inf') # max score to reach end if we start at idx i
            # so table[i] = nums[i] + max of k table vals after
        table[N - 1] = nums[N - 1]
        heap = [[-nums[N - 1], N - 1]]
        for idx in range(N - 2, -1, -1):
            while idx + k < heap[0][1]:
                heapq.heappop(heap)
            negVal, nIdx = heap[0]
            table[idx] = nums[idx] - negVal
            heapq.heappush(heap, [-table[idx], idx])
        return table[0]






        return 

        
