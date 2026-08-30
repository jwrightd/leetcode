class Solution(object):
    def sumDecoded(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        
        def decode(num):
            width = num % 10
            d = num // 10

            strD = str(d)
            x = int(strD[:width])
            y = int(strD[width:])
                
            
            return pow(x,y, 10 ** 9 + 7)

        for num in nums:
            total += decode(num)

        return total % (10 ** 9 + 7)
