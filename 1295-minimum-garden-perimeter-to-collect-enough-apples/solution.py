class Solution(object):
    def minimumPerimeter(self, neededApples):
        """
        :type neededApples: int
        :rtype: int
        """
        # this is just math I think
        # we need a function to check if a certain perim/square size works
        # then Bin search it   (2r(r+1)(2r+1)
        def applesInSquare(r):
            return 2 * r * (r + 1) * (2 * r + 1)
        lower, higher = 1, int(neededApples ** 1/3) + 1
        best = higher
        while lower <= higher:
            mid = (lower + higher)//2
            result = applesInSquare(mid)
            if result >= neededApples:
                best = mid
                higher = mid - 1
            else:
                lower = mid + 1

        return 8 * best


        
        
