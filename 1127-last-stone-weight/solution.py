class Solution(object):
    def lastStoneWeight(self, stones):
        stones.sort()
        while len(stones) > 1:
            n = len(stones)
            diff = (stones[n - 1] - stones[n - 2]) if stones[n - 1] > stones[n - 2] else stones[n - 2] - stones[n - 1]
            stones.pop()
            stones.pop()
            idx = 0
            while idx < n - 2 and stones[idx] < diff:
                idx += 1
            stones = stones[:idx] + [diff] + stones[idx:]
        return stones[0]
        """
        :type stones: List[int]
        :rtype: int
        """
        
