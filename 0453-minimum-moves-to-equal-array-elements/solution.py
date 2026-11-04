class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # same as decrement one element
        smallest = float('inf')
        for i in nums:
            smallest = min(i, smallest)
        tot = 0
        for i in nums:
            tot += (i - smallest)
        return tot

