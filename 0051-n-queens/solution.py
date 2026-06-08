class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def validBoard(board):
            #diag, row, col
            #find four queens
            #find the squares they touch, put them in set
            #if any of queens are in those squares, does not work
            queens = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == "Q":
                        queens.append((i, j))
            
            squares = set()
            for q in queens:
                i, j = q
                temp = []

                for k in range(n):
                    if k != j: 
                        temp.append((i, k))
                    if k != i:
                        temp.append((k, j))

                for k in range(1, n):
                    if i + k < n and j + k < n:
                        temp.append((i + 1, j + 1))
                    if i + k < n and j - k > -1:
                        temp.append((i + k, j - k))
                    if i - k > -1 and j + k < n:
                        temp.append((i - k, j + k))
                    if i - k > -1 and j - k > -1:
                        temp.append((i - k, j - k))
                for i, j in temp:
                    squares.add(n * i + j)
            for i, j in queens:
                if n * i + j in squares:
                    return False
            return True            

        def backtrack(board, result, numQ):
            if numQ == n:
                tmp = []
                for i in board:
                    tmp.append("".join(i))
                result.append(tmp)
                return
            elif numQ == n:
                return

            for i in range(n):
                tmp = board[numQ][i]
                board[numQ][i] = "Q"
                #print(board)
                if validBoard(board):
                    backtrack(board, result, numQ + 1)
                board[numQ][i] = "."

        nqueens = []
        board = [["."] * n for x in range(n)]
        #print(board)
        #print(validBoard([['.', 'Q', '.', '.'], ['.', '.', '.', 'Q'], ['Q', '.', '.', '.'], ['.', '.', 'Q', '.']]))
        backtrack(board, nqueens, 0)
        return nqueens           

        
