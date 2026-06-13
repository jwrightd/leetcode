class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dp problem
        # either we skip or rob
        # 
        table = [-1 for i in range(len(nums) + 2)]
        print(table)

        def dfs(i):
            if i >= len(nums):
                return 0
            #either skip or take
            skip = 0
            take = 0
            if table[i + 2] != -1:
                take = nums[i] + table[i + 2]
            else:
                tmp = dfs(i + 2)
                table[i + 2] = tmp
                take = tmp + nums[i]
            if table[i + 1] != -1:
                skip = table[i + 1]
            else:
                tmp = dfs(i + 1)
                table[i + 1] = tmp
                skip = tmp
            table[i] = max(skip, take)
            return table[i]
        res = dfs(0)
        return res
