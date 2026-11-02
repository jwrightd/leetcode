class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #just minheap maxheap ez
        import heapq
        posNums = [i for i in nums]
        negNums = [-i for i in nums]
        N = len(nums)
        heapq.heapify(posNums)
        heapq.heapify(negNums)
        
        res = []
        for i in range(N//2):
            res.append(heapq.heappop(posNums))
            res.append(-heapq.heappop(negNums))
        if N % 2 == 1:
            res.append(heapq.heappop(posNums))
        
        for i in range(N):
            nums[i] = res[i]


