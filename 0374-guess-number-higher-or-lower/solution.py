# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        myNum = (low + high) // 2
        res = guess(myNum)
        while res != 0:
            myNum = (low + high) // 2
            res = guess(myNum)
            if res == 1:
                low = myNum + 1
            elif res == -1:
                high = myNum - 1
            
            

        return myNum

        
