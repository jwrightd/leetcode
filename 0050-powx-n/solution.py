class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        rng = n if n > 0 else -n
        ret = 1.0
        while rng > 0:
            if 1 & rng:
                ret *= x
            x *= x

            rng >>= 1
        return ret if n > 0 else 1.0/ret


        
        
