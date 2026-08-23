class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # ok so we partition into two equal subsets
        # or as close as possible
        # find max weight that is not greater than total sum / 2

        target = sum(stones)//2
        N = len(stones)
        cache = {}
        def dfs(i, val):
            if val > target:
                return 0
            if i == N:
                return val
            if (i, val) in cache:
                return cache[(i, val)]
            skip = dfs(i + 1, val)
            choose = dfs(i + 1, val + stones[i])
            cache[(i, val)] = max(skip, choose)
            return max(skip, choose)
        return sum(stones) - 2 * dfs(0,0)
        
