class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # i think key insight is that you need ot have the reversed string also in the list 
        reverses = set()
        counts = {}
        res = 0
        for wd in words:
            counts[wd] = counts[wd] + 1 if wd in counts else 1
            reverses.add(wd[::-1])
        cPair = True
        for wd in words:
            if wd in reverses:
                if wd == wd[::-1]:
                    if counts[wd] % 2 == 0:
                        res += counts[wd] * 2
                        
                    else:
                        if cPair:
                            res += counts[wd] * 2
                            cPair = False
                        else:
                            res += (counts[wd] - 1) * 2

                else:
                    res += min(counts[wd], counts[wd[::-1]]) * 4
            counts[wd] = 0

        return res
