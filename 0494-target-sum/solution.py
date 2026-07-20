class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dfs/backtrack + dp?

        # what exactly are we storing tho
        # we store (idx, curr_sum) -> numWays

        dp = {}
        N = len(nums)
        def dfs(i, curr):
            #print(i, curr)
            if (i, curr) in dp:
                return dp[(i, curr)]
            if i == N and curr == target:
                return 1
            elif i == N and curr != target:
                return 0
            
            # dfs with (i + 1)
            add = dfs(i + 1, curr + nums[i])
            sub = dfs(i + 1, curr - nums[i])
            dp[(i, curr)] = add + sub
            return add + sub

        
        return dfs(0, 0)
