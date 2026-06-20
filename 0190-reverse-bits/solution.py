class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        counter = 1
        for i in range(32):     
            current_bit = (n & counter != 0)
            result = ((result << 1) | current_bit)
            counter *= 2   
        return result
