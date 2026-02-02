class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zeroes = []
        for a in range(len(matrix)):
            for b in range(len(matrix[0])):
                if matrix[a][b] == 0:
                    zeroes.append([a, b])
        for z in zeroes:
            a, b = z
            #row
            for i in range(n):
                matrix[a][i] = 0
            for i in range(m):
                matrix[i][b] = 0
                

        
