class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #lets do with math

        highest = max(nums)
        if len(nums) != highest:
            return highest + 1
        expected = highest * (highest + 1) / 2
        val = expected - sum(nums)
        return val if val != 0 else 0
        #n * (n + 1)/2
        
