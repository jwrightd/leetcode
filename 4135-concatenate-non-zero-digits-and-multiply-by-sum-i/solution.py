class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        stk = []

        while n > 0:
            unit = n % 10
            n = n // 10
            if unit != 0:
                stk.append(unit)
        
        newNum = 0
        ctr = 0
        stkSum = sum(stk)
        for digit in stk:
            newNum += digit * 10 ** ctr
            ctr += 1
        
        return newNum * stkSum

        
