class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        

        table = [-1] * (n + 2)


        def dfs(i, end):
            if i >= end:
                return 0

            #skip or take
            if table[i + 1] != -1:
                skip = table[i + 1]
            else:
                skip = dfs(i + 1, end)
                table[i + 1] = skip
            if table[i + 2] != -1:
                take = table[i + 2] + nums[i]
            else:
                res = dfs(i + 2, end)
                table[i + 2] = res
                take = nums[i] + table[i + 2]
            table[i] = max(take, skip)
            return table[i]
        dfs(0, n - 1)
        first = table[0]
        table = [-1] * (n + 2)
        dfs(1, n)
        second = table[1]

        return max(first, second)
        
        
