class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        runSum = 0
        N = len(nums)
        for idx in range(N - 1):
            current, nextNum = nums[idx], nums[idx + 1]
            if nextNum >= current:
                continue
            runSum += (current - nextNum)
        return runSum

