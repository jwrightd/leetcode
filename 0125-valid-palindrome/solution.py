class Solution(object):
    def isPalindrome(self, s):
        valids = "1234567890qwertyuiopasdfghjklzxcvbnm"
        s = s.lower()
        s = "".join([s[i] for i in range(len(s)) if s[i] in valids])
        p1 = 0
        p2 = len(s) - 1
        while p2 > p1:
            if s[p1] != s[p2]:
                return False
            p2 -= 1
            p1 += 1
        return True
        """
        :type s: str
        :rtype: bool
        """
        
