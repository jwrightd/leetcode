class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        # need monotonically increasing stack looking to the right
        # so we process R to L
        # maintain increasing
        # take stack size at each point
        N = len(heights)
        stk = []
        res = [0 for i in range(N)]
        for right in range(N - 1, -1, -1):
            cnt = 0
            while stk and heights[right] > stk[-1]:
                stk.pop(-1)
                cnt += 1
            if stk:
                cnt += 1
            res[right] = cnt
            stk.append(heights[right])
        return res
