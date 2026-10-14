class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        valid = 0
        N = len(nums)
        left = 0
        used = 0
        for right in range(N):
            if nums[right] == 0:
                used += 1
            while used > k:
                if nums[left] == 0:
                    used -= 1
                left += 1
            valid = max(valid, right - left + 1)
        return valid
        
