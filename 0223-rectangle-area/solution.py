class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        # just inc exclusion
        tot = abs(ax1 - ax2) * abs(ay1 - ay2) + abs(bx1 - bx2) * abs(by1 - by2)
        # now check for overlap
        if ax2 < bx1 or ay1 > by2:
            return tot # no overlap
        
        width= max(0,min(ax2,bx2) - max(ax1,bx1))
        height = max(0,min(ay2,by2) - max(ay1,by1))


        return tot - width * height
        
