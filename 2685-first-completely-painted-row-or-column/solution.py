class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0])

        row = {}
        col = {}

        for i in range(m):
            for j in range(n):
                num = mat[i][j]
                row[num] = i
                col[num] = j
        
        rowLeft = {}
        colLeft = {}
        for i in range(m):
            rowLeft[i] = n
        for i in range(n):
            colLeft[i] = m
        count = 0
        for num in arr:
            rowN = row[num]
            colN = col[num]
            rowLeft[rowN] -= 1
            colLeft[colN] -= 1
            if rowLeft[rowN] == 0 or colLeft[colN] == 0:
                return count

            count += 1


                

        
