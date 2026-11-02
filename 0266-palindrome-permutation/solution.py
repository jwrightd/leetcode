class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # only one can be odd, rest must be even
        freq = defaultdict(int)
        for i in s:
            freq[i] += 1
        oddCnt = 0
        for v in freq:
            if freq[v] % 2 == 1:
                oddCnt += 1
            if oddCnt > 1:
                return False
        return True
