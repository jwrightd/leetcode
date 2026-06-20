class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #sort is nlogn
        #but if we use PQ, we just heapify and then pop off k or k - 1 or something
        import heapq
        # we want max heap, so:
        neg_nums = [-i for i in nums]
        heapq.heapify(neg_nums)
        for i in range(k - 1):
            heapq.heappop(neg_nums)
        return -heapq.heappop(neg_nums)
