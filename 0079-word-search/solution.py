class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def find_first():
            ret = []
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word[0]:
                        ret.append((i, j))
            return ret

        def children(i, j):
            ret = []
            if i != 0:
                ret.append((i - 1, j))
            if j != 0:
                ret.append((i, j - 1))
            if i != len(board) - 1:
                ret.append((i + 1, j))
            if j != len(board[0]) - 1:
                ret.append((i, j + 1))
            return ret

        #backtracking
        def backtrack(i, j, current):            
            if board[i][j] != word[current]:
                return False
            if current == len(word) - 1:
                return True
            
            save = board[i][j]
            board[i][j] = "#"

            c = children(i, j)
            for child in c:
                x, y = child
                if board[x][y] != "#":
                    res = backtrack(x, y, current + 1)
                    if res == True:
                        board[i][j] = save
                        return True
            board[i][j] = save
            return False
        
        possible = find_first()
        for i in possible:
            x, y = i
            res = backtrack(x, y, 0)
            if res == True:
                return True
        return False
# A B C E
# S F E S
# A D E E
