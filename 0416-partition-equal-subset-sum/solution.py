class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # we can think about this as choosing which elements should be in one subset
        # (that is half the sum)
        # in other words, can we find some number of elements that sum to half of the sum of overall array

        total = sum(nums)
        
        if total % 2 == 1:
            return False
        
        total = total // 2 # true total each array sums to
        n = len(nums)
        # maybe we simply do choose/skip algo with DP and DFS

        cache = {}

        def dfs(tot, i):
            if tot == total:
                return True

            if i == n or tot > total:
                return False
            if (tot + nums[i], i + 1) not in cache:
                choose = dfs(tot + nums[i], i + 1)# choose
                cache[(tot + nums[i], i + 1)] = choose
            else:
                choose = cache[(tot + nums[i], i + 1)]
            if choose:
                return True
            if (tot, i + 1) not in cache:   
                skip = dfs(tot, i + 1) # skip
                cache[(tot, i + 1)] = skip
            else:
                skip = cache[(tot, i + 1)]
            return skip
        
        return dfs(0, 0)
            


