class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #let's try greedy
        #idea: min and max open
        # if max ever < 0, false
        low = high = 0
        length = len(s)
        for i in range(length):
            if s[i] == "(":
                low += 1
                high += 1
            elif s[i] == ")":
                low -=1
                high -=1
            else: #*
                low -= 1
                high += 1
            if high < 0:
                return False
            if low < 0:
                low = 0
        return low == 0
