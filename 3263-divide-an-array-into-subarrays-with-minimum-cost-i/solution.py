class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #always first element + smallest two elements
        firstEl = nums[0]
        copyNums = [nums[i] for i in range(1, len(nums))]
        copyNums.sort()
        return firstEl + copyNums[0] + copyNums[1]
        
