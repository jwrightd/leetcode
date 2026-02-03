class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        #do binary search
        low = 0
        high = m * n - 1
        mid = (low + high)//2
        tmp = -1
        while (tmp != mid):
            tmp = mid
            current = matrix[mid//n][mid % n]
            if current == target:
                return True
            if target > current:
                low = mid + 1
            elif target < current:
                high = mid - 1
            mid = (low + high)//2
        return False
            

        
