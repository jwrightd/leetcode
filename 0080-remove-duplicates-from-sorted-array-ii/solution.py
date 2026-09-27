class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentElement = nums[0]
        currCount = 1
        placing = 1
        processing = 1

        N = len(nums)

        while processing < N:
            if nums[processing] == currentElement:
                currCount += 1
            else:
                currentElement = nums[processing]
                currCount = 1
            nums[placing] = currentElement
            # if currcount > 2, placing stays same
            if currCount <= 2:
                placing += 1
            processing += 1
        return placing
                
            

