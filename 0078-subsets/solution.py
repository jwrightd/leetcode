class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def recur(ind):
            if len(nums) == ind:
                ret.append(current[:])
                return

            recur(ind + 1) #nonpick

            current.append(nums[ind])
            recur(ind + 1) # pick

            current.pop()


        current = []
        ret = []
        recur(0)
        return ret
        
    
