class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        #this is like area fill, we need at least one O to be on the edge for it to not be surrounded
        def getNeighbors(i, j):
            neigh = []
            if i - 1 >= 0:
                neigh.append((i - 1, j))
            if i + 1 < m:
                neigh.append((i + 1, j))
            if j != 0:
                neigh.append((i, j - 1))
            if j != n - 1:
                neigh.append((i, j + 1))
            return neigh
        Xs = []
        Os = []
        currentArea = []
        def areaFill(i, j):
            if board[i][j] != "O":
                return False
            board[i][j] = "."
            currentArea.append((i, j))
            neighbors = getNeighbors(i, j)

            edge = i == 0 or i == m - 1 or j == 0 or j == n - 1
            for a, b in neighbors:
                edge = areaFill(a,b) or edge
            return edge


        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    res = areaFill(i, j)
                    if res:
                        for x,y in currentArea:
                            Os.append((x,y))
                    else:
                        for x,y in currentArea:
                            Xs.append((x,y))
                    currentArea = []
        for x, y in Xs:
            board[x][y] = "X"
        for x, y in Os:
            board[x][y] = "O"



