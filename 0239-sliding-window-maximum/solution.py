class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        output = []
        
        #strictly monotonic queue
        #queue
        length = len(nums)
        queue = []
        for i in range(length):
            
            
            while queue and (nums[queue[-1]] <= nums[i] or i - queue[0] >= k):
                if nums[queue[-1]] <= nums[i]:
                    queue.pop(-1)
                else:
                    queue.pop(0)
            
            queue.append(i)
            if i >= k - 1:
                output.append(nums[queue[0]])
        return output
        
