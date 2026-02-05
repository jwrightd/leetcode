class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        def backtrack(i):

            if i == len(nums):
                ret.append(curr[:])
                return 
            
            n = i
            while n + 1 < len(nums) and nums[n] == nums[n + 1]:
                n += 1
            backtrack(n + 1) # non pick

            curr.append(nums[i])
            backtrack(i + 1)
            curr.pop()
        

        curr = []
        ret = []
        backtrack(0)
        return ret
