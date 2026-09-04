class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # iterate until end of t, then check rest of s
        sptr, tptr, m, n = 0, 0, len(s), len(t)
        while sptr < m and tptr < n:
            if s[sptr] == t[tptr]:
                tptr += 1
            sptr += 1
        return n - tptr
        
