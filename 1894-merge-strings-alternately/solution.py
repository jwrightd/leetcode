class Solution(object):
    def mergeAlternately(self, word1, word2):
        l1 = len(word1)
        l2 = len(word2)
        smaller = l2 if l1 > l2 else l1
        bigWord = word1 if l1 > l2 else word2
        st = ""
        for i in range(smaller):
            st = st + word1[i] + word2[i]
        return st + bigWord[smaller:]
    
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
    
        
