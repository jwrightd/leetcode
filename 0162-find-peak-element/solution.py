class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # finding some index s.t nums[i - 1] < nums[i] > nums[i + 1]
        # clear bin search I think
        # we need a local max basically
        # we are guaranteed to have one in the array
        # so we should bin search the bigger side
        N = len(nums)
        if N == 1:
            return 0
        if N == 2:
            return 0 if nums[0] > nums[1] else 1
        left, right = 0, N - 1
        while left < right:
            mid = (left + right)//2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return right
