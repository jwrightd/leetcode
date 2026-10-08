class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        # this is just 2ptr and counter
        counter = 0
        N = len(nums)
        for start in range(N):
            left, right = start + 1, N - 1
            newTgt = target - nums[start]
            best = float('inf')
            tmp = 0 
            while left < right:
                if nums[right] + nums[left] >= newTgt:
                    right -= 1
                else:
                    counter += (right - left)
                    left += 1




        return counter
