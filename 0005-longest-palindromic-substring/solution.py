class Solution(object):

    def longestPalindrome(self, s):
        slen = len(s)
        length = 0
        saved = ""
        for i in range(slen):
            for count in range(i, slen + 1):
                current = s[i:count]
                if current[::-1] == current and len(current) > length:
                    saved = current
                    length = len(current)
        return saved
                
        """
        :type s: str
        :rtype: str
        """
    
        
