class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        #backtracking
        #trick is how to prune
        
        #trie, not cache
        trie = {}

        for word in words:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["$"] = word

        wordsFound = set()
        m = len(board)
        n = len(board[0])

        def children(i, j):
            output = []
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if  x >= 0 and x < m and y >= 0 and y < n and board[x][y] != ".":
                    output.append((x,y))
            return output

        def backtrack(node, i, j):
            if "$" in node:
                wordsFound.add(node["$"])
                # can't just return, imagine oat and oath are both valid words, for example
            choices = children(i, j)
            for x, y in choices: 
                current = board[x][y]
                if current in node:
                    tmp = board[x][y]
                    board[x][y] = "."
                    backtrack(node[current], x, y)
                    board[x][y] = tmp
        for i in range(m):
            for j in range(n):
                tmp = board[i][j]
                if tmp in trie:
                    board[i][j] = "."
                    backtrack(trie[tmp], i, j)
                    board[i][j] = tmp
        
        return list(wordsFound)
