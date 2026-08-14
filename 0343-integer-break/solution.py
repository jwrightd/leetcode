class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        # for x, y > 1, xy >= x + y
        # so if we can decompose to more parts, this is better'
        # so for anything > 4, we should decompose
        # 3 * 3 = 9 > 8 = 2 * 2 * 2, so we should choose 3 over 2
        # but we need case because k >= 2, so for n in [2, 6] you have predetermined res
        res = [1, 2, 4, 6, 9]
        val = 1
        while n > 6:
            val *= 3
            n -= 3
                
        return val * res[n - 2]

        


        
