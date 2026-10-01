class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # ok we must do at least k robberies
        # bin search?

        N = len(nums)

        def isValid(mid):
            idx, count = 0, 0
            while idx < N:
                if nums[idx] <= mid:
                    count += 1
                    idx += 2
                else:
                    idx += 1
            return count >= k

        low, high = min(nums), max(nums)
        best = -1

        while low <= high:
            mid = (low + high)//2

            if isValid(mid):
                best = mid
                high = mid - 1
            else:
                low = mid + 1
        return best
        
