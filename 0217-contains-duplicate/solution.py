class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        vals = set()
        for i in nums:
            if i in vals:
                return True
            vals.add(i)
        return False
