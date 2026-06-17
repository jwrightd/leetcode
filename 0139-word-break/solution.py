class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        #graph problem

        #brute force - dfs
        #for i in wordDict:
        # if i in s:
        # update s, recur

        #now, i need memo
        table = [-1 for i in range(len(s) + 1)]
        
        def dfs(i):
            if i == len(s):
                return True
            for word in wordDict:
                length = len(word)
                if i + length <= len(s) and s[i:i + length] == word:
                    if table[i + length] != -1:
                        res = table[i + length]
                    else:
                        res = dfs(i + length)
                        table[i + length] = res
                    if res:
                        return True
            return False
        r = dfs(0)
        return r
        
