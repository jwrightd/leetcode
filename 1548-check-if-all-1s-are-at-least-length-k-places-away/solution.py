class Solution(object):
    def kLengthApart(self, nums, k):
        last = -1
        for idx, val in enumerate(nums):
            if nums[idx] == 1 and idx - last <= k and last != -1:
                return False
            if nums[idx] == 1:
                last = idx
        return True
