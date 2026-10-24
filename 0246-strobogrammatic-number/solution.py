class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        N = len(num)
        pairs = {}
        pairs["6"] = "9"
        pairs["9"] = "6"
        pairs["8"] = "8"
        pairs["1"] = "1"
        pairs["0"] = "0"
        for i in range(N//2 + 1):
            curr = num[i]
            if curr not in pairs:
                return False
            match = num[N - i - 1]
            if pairs[curr] != match:
                return False
            
            
        return True



