class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        cnt = 0
        visited = set()
        M, N = len(board), len(board[0])

        def dfs(i, j):     
            if (i, j) in visited:
                return 0
            if board[i][j] == ".":
                return 0
            board[i][j] = "."
            visited.add((i, j))
            for y, x in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= y < M and 0 <= x < N and board[y][x] == "X":
                    dfs(y, x)
            return 1
        for i in range(M):
            for j in range(N):
                cnt += dfs(i, j)

        return cnt
        
