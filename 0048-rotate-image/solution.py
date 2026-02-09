class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # swap horizontally then transpose
        n = len(matrix)
        #1 horizontal
        for i in range(len(matrix)//2):
            top = matrix[i]
            bottom = matrix[n - i - 1]
            matrix[i] = bottom
            matrix[n - i - 1] = top
        #2 transpose
        for i in range(n):
            for j in range(i + 1, n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp


        
