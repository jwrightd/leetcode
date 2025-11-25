class Solution(object):
    def longestCommonPrefix(self, strs):
        sorted_strs = sorted(strs, key = len, reverse = True)
        stem = sorted_strs[0]
        for i in range(0, len(strs) - 1):
            nextWord = sorted_strs[i + 1]
            while nextWord != stem[:len(nextWord)]:
                nextWord = nextWord[:len(nextWord) - 1]
            stem = nextWord
        return stem



        """
        :type strs: List[str]
        :rtype: str
        """
        
