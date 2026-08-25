class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        doubled = [i for i in nums]
        return doubled + nums
        
