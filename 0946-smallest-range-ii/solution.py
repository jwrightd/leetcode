class Solution(object):
    def smallestRangeII(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        
        N = len(nums)
        #if N == 1:
        #   return 0
        minScore = nums[-1] - nums[0]
        # treat each index i as partition element
        # then we treat it as add k from all before, sub k to all after and i
        # then we can derive new max and min
        # min is min(nums[0] + k, nums[i] - k)
        # max is max(nums[i - 1] + k, nums[-1] - k)
        for i in range(1, N):
            currMin = min(nums[0] + k, nums[i] - k)
            currMax = max(nums[i - 1] + k, nums[-1] - k)
            minScore = min(minScore, currMax - currMin)
        return minScore

        
