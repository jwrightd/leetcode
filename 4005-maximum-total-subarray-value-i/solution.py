class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #isnt this just finding the max subarray and x by k
        return (max(nums) - min(nums)) *k
        
