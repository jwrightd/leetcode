class Solution(object):
    def singleNumber(self, nums):
        temp = 0
        for i in nums:
            temp = temp ^ i
        return temp
        """
        :type nums: List[int]
        :rtype: int
        """
        
