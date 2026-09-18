class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # when you have the 1 and 3, you need to find a two
        # so do monotonic stack for the 1,3  
        # what if we went reverse and did 231 pattern
        # then monotonic decreasing stack for 3 candidates
        # var for the 2
        # then we done if ew find 1
        stk = []
        two = float('-inf')
        rev = nums[::-1]
        for val in rev:
            if val < two:
                return True
            while stk and val > stk[-1]:
                two = stk.pop(-1)
            stk.append(val)
        return False
        
