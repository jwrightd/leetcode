class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # treat every index as the left corner of a size i square
        # start at i = 1, increase boundary and increment count
        m = len(matrix)
        n = len(matrix[0])

        def numSquares(i, j):
            size = 0
            visited = set()
            if matrix[i][j] == 1:
                size += 1
            else:
                return 0
            visited.add((i, j))
            nI, nJ = i - 1, j + 1
            while nI >= 0 and nJ < n:
                for a in range(nI, i + 1):
                    for b in range(j, nJ + 1):
                        if (a, b) not in visited:
                            if matrix[a][b] == 0:
                                return size
                #print(i, j, nI, nJ)
                size += 1
                nI -= 1
                nJ += 1
            return size
            # track upper corner maybe

            return

        count = 0
        for i in range(m):
            for j in range(n):
                count += numSquares(i, j)
        return count
        
        
