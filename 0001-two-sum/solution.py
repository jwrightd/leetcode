class Solution(object):
    def twoSum(self, nums, target):
        h = dict()
        for ind, val in enumerate(nums):
            h[val] = ind
        for idx, v in enumerate(nums):
            if target - v in h and h[target - v]!=idx:
                return [h[target - v], idx]
    
        
