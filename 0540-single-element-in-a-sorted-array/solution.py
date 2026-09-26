class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # bin search, pairs are together
        # so if thing at mid has no pair, we found it
        # if thing at mid has pair to the left, we search right
        # else we search left
        N = len(nums)
        if N == 1:
            return nums[0]
        
        low, high = 0, N - 1
        
        while low <= high:
            
            mid = (low + high)//2
            pairEnd = mid + 1 if mid + 1 < N and nums[mid + 1] == nums[mid] else mid
            if (mid == 0 and nums[1] != nums[0]) or (mid == N - 1 and nums[N - 1] != nums[N - 2]) or (mid != 0 and nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1]):
                return nums[mid]
            if pairEnd % 2 == 1:
                low = mid + 1
            else:
                high = mid - 1
        return nums[mid]
        
        

