class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        #bfs
        if endWord not in wordList:
            return 0
        
        visited = set()
        wordSet = set()
        q = []

        for i in wordList:
            wordSet.add(i)
        
        def children(word):
            alpha = "qwertyuiopasdfghjklzxcvbnm"
            ret = []
            for i in range(len(word)):
                for j in range(26):
                    newWord = word[:i] + alpha[j] + word[i + 1:]
                    if newWord in wordSet:
                        ret.append(newWord)
            return ret

        q.append((beginWord, 1))
        visited.add(beginWord)
    
        while len(q) > 0:
            curr, n = q.pop(0)
            if curr == endWord:
                return n
            for c in children(curr):
                if c not in visited:
                    q.append((c, n + 1))
                    visited.add(c)
        return 0

        


        
