class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        low = 0
        high = N - 1
        mid = (low + high)//2
        while low <= high:
            mid = (low + high)//2
            #print(mid)
            if nums[mid] == target:
                return mid
            if (mid == 0 and target < nums[mid]):
                return 0
            if (0 <= mid < N - 1 and nums[mid] < target < nums[mid + 1]):
                return mid + 1
            if  (mid == N - 1 and nums[mid] < target):
                return N
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
            

        
