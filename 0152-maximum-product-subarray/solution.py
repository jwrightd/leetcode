class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # kadane's algo, but modified for * instead of +
        # we need both max and min (min can be * by neg to get biggest)
        curr_max = nums[0]
        curr_min = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            tmp = curr_max
            curr_max = max(nums[i], curr_max * nums[i], curr_min * nums[i])
            curr_min = min(nums[i], curr_min * nums[i], tmp * nums[i])
            global_max = max(global_max, curr_max)
        return global_max
            
