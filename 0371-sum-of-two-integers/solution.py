class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # we need to do a bitwise add
        # a = 1, b = 2
        #  0001 
        # +0010
        # a ^ b = 0011

        # 0010 
        #+0011
        # 0101
        # we do AND and then left shift to get 0100 and then add XOR

        # 20 + 30
        #  1 0100
        # +1 1110
        # 
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        carry = (a & b) << 1
        pSum = a ^ b
        sumNums = carry | pSum
        while carry != 0:
            a = pSum
            b = carry
            carry = ( (a & b) << 1) & MASK
            pSum = (a ^ b ) & MASK
        return  pSum if pSum <= MAX_INT else pSum - (1 << 32)
        
