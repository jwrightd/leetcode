class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # n in [1, 20]
        output = [[0] * n for i in range(n)]
        # right, down, left, up cycle
        # we go from nxn to (n - 2) x (n - 2)
        curr = 0
        i = 0
        j = -1
        horiz = n
        vert = n
        while curr < n ** 2:
            # right
            for num in range(horiz):
                curr += 1
                j += 1
                output[i][j] = curr
            vert -= 1
            #print(output)
            # down
            for num in range(vert):
                curr += 1
                i += 1
                output[i][j] = curr
            horiz -= 1
            #print(output)

            #left
            for num in range(horiz):
                curr += 1
                j -= 1
                output[i][j] = curr
            vert -= 1
            #print(output)
            
            # up
            for num in range(vert):
                curr += 1
                i -= 1
                output[i][j] = curr
            horiz -=1
            #print(output)

        return output
