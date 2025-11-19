class Solution(object):
    def findFinalValue(self, nums, original):
        return self.findFinalValue(nums, original * 2) if original in nums else original
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        
