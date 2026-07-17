class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        output = [[] for i in range(n)]
        for i in range(m):
            for j in range(n):
                output[j].append(matrix[i][j])
        return output
        
