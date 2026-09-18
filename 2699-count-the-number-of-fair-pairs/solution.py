class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        N = len(nums)
        count = 0

        def pairs(tgt):
            left, right = 0, N - 1
            count = 0
            while left < right:
                if nums[left] + nums[right] <= tgt:
                    count += (right - left)
                    left += 1
                else:
                    right -= 1
            return count


        return pairs(upper) - pairs(lower - 1)

        




        
        
        
