class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mx = 0
        nextJump = nums[0]
        for i in range(len(nums)):
            jump = nums[i] + i
            mx = max(jump, mx)

            if mx >= len(nums) - 1:
                return True
            if nums[i] == 0 and i == nextJump and mx <= nextJump:
                return False
            
            

            if i == nextJump:
                nextJump = mx
                

            
        return False
        
