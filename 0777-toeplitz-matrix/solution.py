class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # algo:
        # lowkey probably start bottom left, go diag, then go up
        # once you hit top left, you go right
        # helper fxn for getting diagonal probabl is good
        m = len(matrix)
        n = len(matrix[0])
        def getDiag(i, j):
            output = set()
            output.add(matrix[i][j])
            x, y = i + 1, j + 1
            while 0 <= x < m and 0 <= y < n:
                output.add(matrix[x][y])
                x += 1
                y += 1
            return output

        #bottom left
        i = m - 1
        j = 0
        while i >= 0:
            if len(getDiag(i, j)) != 1:
                return False
            i -= 1
        i = 0
        while j < n:
            if len(getDiag(i, j)) != 1:
                return False
            j += 1
        return True


            
