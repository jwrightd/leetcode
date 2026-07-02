class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # we want to do DP here with choose/not choose
        # dp[i] is LIS ending at i
        n = len(nums)
        table = [1] * n
        
        for i in range(n):
            for j in range(i): # prev elements
                if nums[i] > nums[j]:
                    table[i] = max(table[i], table[j] + 1) #either current subseq or j and add ith element
        return max(table)



