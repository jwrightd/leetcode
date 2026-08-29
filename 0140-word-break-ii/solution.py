class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # make trie
        # recur thru

        trie = {}
        for word in wordDict:
            temp = trie
            for letter in word:
                if letter in temp:
                    temp = temp[letter]
                else:
                    temp[letter] = {}
                    temp = temp[letter]    
            temp["#"] = word # end of word

        output = set()

        N = len(s)
        def dfs(i, node, sentence):
            if i == N:
                if "#" in node:
                    sentence.append(node["#"])
                    output.add(" ".join(sentence))
                    sentence.pop()
                return

            nextCh = s[i]

            if nextCh in node:
                neighbor = node[nextCh]
                if "#" in neighbor:
                    sentence.append(neighbor["#"])
                    dfs(i + 1, trie, sentence)
                    sentence.pop() # backtrack
                dfs(i + 1, neighbor, sentence)

        dfs(0, trie, [])
        return list(output)

