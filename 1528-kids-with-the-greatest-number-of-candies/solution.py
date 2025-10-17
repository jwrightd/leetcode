class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        m = max([x for x in candies])
        ret = []
        for x in candies:
            if x + extraCandies >= m:
                ret.append(True)
            else:
                ret.append(False)
        return ret
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
