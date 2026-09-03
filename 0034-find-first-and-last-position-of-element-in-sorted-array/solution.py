class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # just need two variants of bin search

        N = len(nums)
        if N == 0:
            return [-1, -1]
        def firstInstance(nums, target):
            best = -1
            left, right = 0, N - 1
            mid = (left + right)//2
            while left <= right:
                mid = (left + right)//2
                if nums[mid] == target:
                    best = mid
                    right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1


            return best
        
        def lastInstance(nums, target):
            best = -1
            left, right = 0, N - 1
            mid = (left + right)//2
            while left <= right:
                mid = (left + right)//2
                if nums[mid] == target:
                    best = mid
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return best

        return [firstInstance(nums, target), lastInstance(nums, target)]
