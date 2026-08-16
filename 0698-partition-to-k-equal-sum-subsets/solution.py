class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        N = len(nums)
        tot = sum(nums)
        if tot % k != 0:
            return False
        desired = tot//k
        nums.sort(reverse=True)

        if nums[0] > desired:
            return False
        used = [False] * N


        def dfs(i, k, subsetSum):
            if k == 0:
                return True
    
            if subsetSum == desired:
                return dfs(0, k - 1, 0)

            for idx in range(i, N):
                if used[idx] or nums[idx] + subsetSum > desired:
                    continue

                used[idx] = True

                if dfs(idx + 1, k, subsetSum + nums[idx]):
                    return True

                used[idx] = False
                if subsetSum == 0:
                    break




            return False
        
        return dfs(0, k, 0)
        
