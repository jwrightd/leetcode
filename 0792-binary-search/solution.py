class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        low = 0
        high = N - 1
        mid = (high + low)//2
        # [a,b]
        # 
        while low <= high:
            mid = (high + low)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target: #we go lower half
                high = mid - 1
            else:
                low = mid + 1
        return mid if nums[mid] == target else -1

        
