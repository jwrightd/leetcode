class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        n = len(img1)
        def checkOverlap(i, j): # shift by i, j
            overlap = 0
            for x in range(n):
                for y in range(n):
                    if img1[x][y] == 1 and 0 <= x + i < n and 0 <= y + j < n and img2[x + i][y + j] == 1:
                        overlap += 1
            #print(overlap, i, j)
            return overlap
        largest = 0
        for i in range(n):
            for j in range(n):
                largest = max(largest, checkOverlap(i, j), checkOverlap(-i, -j), checkOverlap(i, -j), checkOverlap(-i, j))

        return largest
                
        
