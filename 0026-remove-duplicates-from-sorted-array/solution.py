class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        last = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != last:
                nums[count] = nums[i]
                count += 1
            last = nums[i]
        return count
            

        
