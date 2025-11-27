class Solution(object):
    ret = []
    def permute(self, nums):
        self.ret = []
        self.recur(nums, len(nums), [])
        return self.ret
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    def recur(self, nums, n, arr):
        if len(arr) == n:
            self.ret.append(arr)
        else:
            for idx, val in enumerate(nums):
                self.recur(nums[:idx] + nums[idx + 1:], n, arr + [val])

        
