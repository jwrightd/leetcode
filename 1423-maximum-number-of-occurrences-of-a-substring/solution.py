class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        N = len(s)
        letters = defaultdict(int)
        subFreqs = defaultdict(int)
        for i in range(minSize - 1):
            letters[s[i]] += 1


        for idx in range(N - minSize + 1):
            letters[s[idx + minSize - 1]] += 1
            # check num letters

            numLetters = 0
            for ltr in letters:
                if letters[ltr] > 0:
                    numLetters += 1
            
            if numLetters <= maxLetters:
                subFreqs[s[idx:idx+minSize]] += 1
            letters[s[idx]] -= 1

        common = 0
        for i in subFreqs:
            common = max(common, subFreqs[i])
        return common

                
            

                
