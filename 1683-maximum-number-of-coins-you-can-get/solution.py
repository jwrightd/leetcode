class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        #greedy strategy, want to have differences as smallas possible
        piles.sort(reverse=True)
        N = len(piles)
        # choose biggest 2, give bob smallest
        iters = N//3
        cnt = 0
        for _ in range(iters):
            cnt += piles[2 * _ + 1]
        return cnt
