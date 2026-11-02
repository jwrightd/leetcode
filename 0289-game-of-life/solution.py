class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 2d neighbor table
        M, N = len(board), len(board[0])
        table = [[0 for _ in range(N)] for _ in range(M)]

        for i in range(M):
            for j in range(N):
                neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i + 1, j + 1), (i + 1, j - 1), (i - 1, j + 1), (i - 1, j - 1)]
                for y, x in neighbors:
                    if 0 <= y < M and 0 <= x < N and board[y][x] == 1:
                        table[i][j] += 1 # valid neighbor
        for i in range(M):
            for j in range(N):
                if board[i][j] == 1 and (table[i][j] < 2 or table[i][j] > 3):
                    board[i][j] = 0
                elif board[i][j] == 1 and (table[i][j] == 2 or table[i][j] == 3):
                    board[i][j] = 1
                elif board[i][j] == 0 and table[i][j] == 3:
                    board[i][j] = 1
