class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        alpha = "abcdefghijklmnopqrstuvwxyz"
        mapping = {}
        for idx, val in enumerate(alpha):
            mapping[val] = 26 - idx
        cnt = 0
        for idx, ch in enumerate(s):
            cnt += (idx + 1) * mapping[ch]

        return cnt
        
