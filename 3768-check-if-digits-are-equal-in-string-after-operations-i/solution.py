class Solution(object):
    def hasSameDigits(self, s):
        while len(s) != 2:
            tmp = ""
            for i in range(len(s) - 1):
                temp = int(s[i]) + int(s[i + 1])
                tmp += str(temp % 10)
            s = tmp
        print(s)
        return s[0] == s[1]
        """
        :type s: str
        :rtype: bool
        """
        
