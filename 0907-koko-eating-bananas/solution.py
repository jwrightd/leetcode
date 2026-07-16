class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        # ok let's consider this
        # idea can be like binary search
        # min speed is 1, max speed is highest piles value
        # do min binary search where we update best value every time we search lower half

        left = 1
        right = max(piles)
        mid = (left + right)//2
        smallest = -1

        def getNumHours(k):
            count = 0
            for i in piles:
                count += (i // k if i % k == 0 else i // k + 1)
            return count
        
        while left <= right:
            if getNumHours(mid) <= h:
                smallest = mid
                right = mid - 1
            else:
                left = mid + 1
            mid = (left + right)//2
        return smallest

        
