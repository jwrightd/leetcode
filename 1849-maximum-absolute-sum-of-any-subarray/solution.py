class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # kadanes
        # but its either max or min sum
        curr_max = 0
        total_max = 0
        for i in nums:
            curr_max += i
            total_max = max(curr_max, total_max)
            if curr_max < 0:
                curr_max = 0

        curr_min = 0
        total_min = 0
        for i in nums:
            curr_min += i
            total_min = min(curr_min, total_min)
            if curr_min > 0:
                curr_min = 0


        return max(total_max, -total_min)
