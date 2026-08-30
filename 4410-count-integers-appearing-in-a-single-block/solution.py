class Solution(object):
    def countSpecialIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # counter
        lastIdx = {}
        valid = set(nums)
        for idx, val in enumerate(nums):
            if val in lastIdx and idx - lastIdx[val] > 1:
                if val in valid:
                    valid.remove(val)
            lastIdx[val] = idx
        return len(valid)
                
                
                
        
