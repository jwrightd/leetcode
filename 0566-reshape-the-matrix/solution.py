class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        # lets turn it into a 1d arr
        output = []
        for i in mat:
            for j in i:
                output.append(j)
        reshaped = []
        count = 0
        for i in range(r):
            reshaped.append(output[count:count + c])
            count += c
        return reshaped


        
