class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ok so we use floyds cycle finding algo
        # we have n + 1 integers, so imagine we have nodes 1 to n, with some missing
        # in the nums array, the next number represents the next node connection
        # so we can kind of make our linked list by taking making fast and slow pointers
        # we check the next number, go to that [index-1]
        # we do this once for slow pointer, twice for fast

        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        secondSlow = nums[0]
        while secondSlow != slow:
            slow = nums[slow]
            secondSlow = nums[secondSlow]
            

        return slow
   
        
