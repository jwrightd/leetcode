class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.words = defaultdict(list)
        for idx, w in enumerate(wordsDict):
            self.words[w].append(idx)
        

    def shortest(self, word1: str, word2: str) -> int:
        i = 0
        j = 0
        n = len(self.words[word1])
        m = len(self.words[word2])
        short = float('inf')
        while i < n and j < m:
            short = min(short, abs(self.words[word1][i] - self.words[word2][j]))
            #print(short, i ,j, n, m)
            if i < n and self.words[word1][i] < self.words[word2][j]:
                i += 1
            elif j < m:
                j += 1
        return short
        
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
