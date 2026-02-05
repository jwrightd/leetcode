class Solution(object):
    def constructTransformedArray(self, nums):
        return [nums[(idx + nums[idx]) % len(nums)] for idx, val in enumerate(nums)]
        
