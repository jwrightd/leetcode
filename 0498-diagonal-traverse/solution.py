class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        output = []
        m = len(mat)
        n = len(mat[0])
        i = j = 0
        inc = True
        #what's our algo?
        # oh wait its easy
        # if we end on top or right border, 

        while len(output) < m * n:
            output.append(mat[i][j])
            if inc:   
                while i - 1 >= 0 and j + 1 < n:
                    output.append(mat[i - 1][j + 1])
                    i -= 1
                    j += 1
            else:
                while i + 1 < m and j - 1 >= 0:
                    output.append(mat[i + 1][j - 1])
                    i += 1
                    j -= 1
            
            # now we need to move to next diagonal
            if inc:
                if j != n - 1:
                    j += 1
                else:
                    i += 1
            else:
                if i != m - 1:
                    i += 1
                else:
                    j += 1
            inc = not inc
        return output
                

