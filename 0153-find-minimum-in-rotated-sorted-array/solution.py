class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #binary search variant
        # when we split, one half is sorted, one is not
        # we want to find smallest element
        # we figure out which is sorted, which is not
        # we compare 
        length = len(nums)
        left = 0
        right = length - 1
        middle = (right + left)//2
        while right > left:

            # we decide which side to look at
            if nums[right] < nums[middle]:
                left = middle + 1
            else:
                right = middle
            middle = (right + left)//2
        return nums[middle]

