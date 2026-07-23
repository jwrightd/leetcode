class Solution(object):
    def shortestWordDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # can have list of idx for w1, w2
        # n2 soln is brute force
        # can we do in nlogn if we sort both?
        # most recent idxs
        same = (word1 == word2)
        w1 = -1
        w2 = -1
        idx = 0
        shortestDist = float('inf')
        n = len(wordsDict)
        alternate = 1
        while idx < n:
            if wordsDict[idx] == word1 and alternate:
                w1 = idx
                if same:
                    alternate = 0
            elif wordsDict[idx] == word2:
                w2 = idx
                if same:
                    alternate = 1
            if w1 != -1 and w2 != -1:
                shortestDist = min(shortestDist, abs(w2 - w1))
            #print(w1, w2)
            idx += 1
        return shortestDist
