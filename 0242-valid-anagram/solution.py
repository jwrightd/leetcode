class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        slen = len(s)
        tlen = len(t)
        if slen != tlen:
            return False
        s_dict = dict()
        t_dict = dict()

        for i in range(slen):
            s_dict[s[i]] = 1 if s[i] not in s_dict else 1 + s_dict[s[i]]
            t_dict[t[i]] = 1 if t[i] not in t_dict else 1 + t_dict[t[i]]

        for i in s_dict:
            if i not in t_dict or t_dict[i] != s_dict[i]:
                return False
        return True
        
