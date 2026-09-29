class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # prefix sum maybe
        # can do two pointer
        # -1 0 1 2 3 4 3 2 1
        # can hash the counts for smallest idx, then check for biggest
        idx_map = {}
        biggest = 0
        N = len(nums)
        nums[0] = -1 if nums[0] == 0 else nums[0]
        for idx, val in enumerate(nums):
            if idx == 0:
                continue
            nums[idx] = nums[idx - 1] + 1 if val == 1 else nums[idx - 1] - 1
        for i in range(N):
            if nums[i] not in idx_map:
                idx_map[nums[i]] = i
            else:
                biggest = max(biggest, i - idx_map[nums[i]])
            if nums[i] == 0:
                biggest = max(biggest, i + 1)
        
        return biggest
            
