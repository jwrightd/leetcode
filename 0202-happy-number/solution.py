class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def nextNum(n):
            val = 0
            while n != 0:
                digit = n % 10
                val += digit ** 2
                n = n//10
            return val

        nums = set()
        while n != 1 and n not in nums:
            nums.add(n)
            n = nextNum(n)
        
        return True if n == 1 else False

        
