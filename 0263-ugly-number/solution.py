class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n > 1:
            if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
                return False
            if n % 2 == 0:
                n = n/2
            elif n % 3 == 0:
                n /= 3
            else:
                n/=5

        return True
