class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # like 2d bin search
        # can bin search rows and cols? should be okay?
        M, N = len(matrix), len(matrix[0])

        for row in range(M):
            low, high = 0, N - 1
            while low <= high:
                mid = (low + high)//2
                if matrix[row][mid] == target:
                    return True
                if matrix[row][mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1

        return False
        
