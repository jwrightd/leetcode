class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #for i in board:
        #    print(i)
        # lets do cols, rows, squares
        #rows first
        for i in range(len(board)):
            curr_row = board[i]
            rowSet = set()
            for n in range(len(board[i])):
                if board[i][n] in rowSet:
                    return False
                if board[i][n] != "." and board[i][n] not in rowSet:
                    rowSet.add(board[i][n])

        #cols
        for i in range(len(board)):
            curr_col = [board[n][i] for n in range(len(board))]
            colSet = set()
            for n in range(len(board)):
                if board[n][i] in colSet:
                    return False
                if board[n][i] != "." and board[n][i] not in colSet:
                    colSet.add(board[n][i])
        
        #squares can do with % adn //
        squares = [i for i in range(0, 9)]
        for i in squares:
            squareSet = set()
            #print("SQUARE", i)
            for j in range(0, 3):
                for k in range(0, 3):
                    r = 3 * (i//3) + j 
                    c = 3 * (i %3) + k
                    #print(board[r][c], "AT", r, c)
                    if board[r][c] in squareSet:
                        return False
                    if board[r][c] != "." and board[r][c] not in squareSet:
                        squareSet.add(board[r][c])
        return True



        
