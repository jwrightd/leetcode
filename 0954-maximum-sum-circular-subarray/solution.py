class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # track min subarray and max subarray

        total = sum(nums)

        max_sum = float('-inf')
        curr_max_sum = 0

        min_sum = float('inf')
        curr_min_sum = 0


        for val in nums:
            curr_max_sum += val
            curr_min_sum += val

            max_sum = max(max_sum, curr_max_sum)
            min_sum = min(min_sum, curr_min_sum)

            if curr_max_sum < 0:
                curr_max_sum = 0
            if curr_min_sum > 0:
                curr_min_sum = 0
        if min_sum == total:
            return max_sum
        return max(max_sum, total - min_sum)

