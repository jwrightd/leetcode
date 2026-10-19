class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """   
        
        def validBoard(board, queens):
            #diag, row, col
            #find four queens
            #find the squares they touch, put them in set
            #if any of queens are in those squares, does not work
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
        
        def backtrack(board, queens):
            if len(queens) == n:
                return 1
            numQ = len(queens)
            tot = 0
            for i in range(n):
                tmp = board[numQ][i]
                board[numQ][i] = "Q"
                queens.append([numQ, i])
                if validBoard(board, queens):
                    tot += backtrack(board, queens)
                board[numQ][i] = "."
                queens.pop(-1)
            return tot
        board = [["."] * n for _ in range(n)]
        tot = 0
        nqueens = []

        return backtrack(board, nqueens)
