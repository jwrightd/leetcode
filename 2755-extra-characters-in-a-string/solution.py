class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        # need to match every char of s to something in dictionary
        # what if we trie the dictionary
        # dfs over the trie
        # check all possible and take min every time
        N = len(s)
        
        trie = {}
        for word in dictionary:
            tmp = trie
            for letter in word:
                if letter not in tmp:
                    tmp[letter] = {}
                tmp = tmp[letter]
            tmp["#"] = 0


        memo = {}

        def dfs(i):
            if i == N:
                return 0
            if i in memo:
                return memo[i]

            # skip or take
            #skip
            res = 1 + dfs(i + 1)

            # take:
            curr = trie
            for idx in range(i, N):
                tgt = s[idx]
                if tgt not in curr:
                    break
                curr = curr[tgt]
                if "#" in curr:
                    res = min(res, dfs(idx + 1))
            memo[i] = res
            return res
                


        return dfs(0)
            


