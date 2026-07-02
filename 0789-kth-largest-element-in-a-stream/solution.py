class KthLargest(object):
    import heapq

    def __init__(self, k, nums):
        self.heap = []
        self.k = k
        for i in nums:
            heapq.heappush(self.heap, i)
            if len(self.heap) > k:
                heapq.heappop(self.heap)

        """
        :type k: int
        :type nums: List[int]
        """
        

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        """
        :type val: int
        :rtype: int
        """
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

#ok, let's think about what DS to use
# we want to have sorted, so maybe we use heap. kth element usually indicates heap
# oh i have an idea, since we only add and never take away, we can just cap heap size at k
# so we have k-size heap at max

# algo:
# make heap
# add until size is k
# top of heap is the kth smallest
# when we add, we jsut add our new node to the heap and pop the top and return new top 
