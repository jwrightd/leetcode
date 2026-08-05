class NumMatrix(object):
    # we need O(1) sum region
    # so obvious ON^2 is just checking the indices
    # i think we can do some sort of prefix sum type thing
    # maybe we prefix sum the cols and the rows seprately
    # [3 3 4 8 10]
    # [5 11 14 16 17]
    # [1 3 3 4 9]
    # [4 5 5 6 13]
    # [1 1 4 4 9]


    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        prefix = [[0 for i in range(n)] for j in range(m)]
        prefix[0][0] = matrix[0][0]
        for i in range(1, n):
            prefix[0][i] = prefix[0][i - 1] + matrix[0][i]
        for i in range(1, m):
            prefix[i][0] = prefix[i - 1][0] + matrix[i][0]
        for i in range(1, m):
            for j in range(1, n):
                prefix[i][j] = matrix[i][j] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]
        self.prefixed = prefix

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 == 0 and col1 == 0:
            return self.prefixed[row2][col2]
        elif row1 == 0:
            return self.prefixed[row2][col2] - self.prefixed[row2][col1 - 1]
        elif col1 == 0:
            return self.prefixed[row2][col2] - self.prefixed[row1 - 1][col2]
        return self.prefixed[row2][col2] - self.prefixed[row1 - 1][col2] - self.prefixed[row2][col1 - 1] + self.prefixed[row1-1][col1 -1]
        

    # [3 3 4 8 10]
    # [8 14 18 24 27]
    # ok i see, we do double prefix sum to get sum from 0,0 to row2, col2
    # then we subtract dps row1 - 1, col2 and dps dps row, col1 - 1
    # and add dps row1 - 1, col1 - 1
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


