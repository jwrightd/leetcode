class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        lenF = len(flowerbed)
        if lenF == 1:
            return True if flowerbed[0] == 0 or n == 0 else False
        count = 0
        if flowerbed[0] + flowerbed[1] == 0:
            count += 1
            flowerbed[0] = 1
        if flowerbed[lenF - 1] + flowerbed[lenF - 2] == 0:
            count += 1
            flowerbed[lenF - 1] = 1
        for i in range(1, lenF - 1):
            if flowerbed[i] != 1 and flowerbed[i - 1] == flowerbed[i + 1] == 0:
                count += 1
                flowerbed[i] = 1
        return True if count >= n else False

        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
