class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # binary search for largest val
        # check items to left and right if applicable
        # if increasing then check right
        # if decreasing check left
        # if it is bigger than both then return
        N = len(arr)
        left, right = 1, N - 2
        mid = (left + right)//2
        while left <= right:

            mid = (left + right)//2
            if arr[mid + 1] < arr[mid] > arr[mid - 1]:
                return mid
            if arr[mid + 1] > arr[mid] > arr[mid - 1]:
                left = mid + 1
            else:
                right = mid - 1
        return left
            



        
