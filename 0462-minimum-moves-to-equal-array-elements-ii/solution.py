class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # greedy
        # find median 
        # dist to median
        nums.sort()
        N = len(nums)
        if N % 2 == 1:
            median = nums[N//2]
            tot = 0
            for i in nums:
                tot += abs(i - median)
            return tot
        else:
            m1, m2 = nums[N//2 - 1], nums[N//2]
            t1, t2 = 0, 0
            for i in nums:
                t1 += abs(i - m1)
                t2 += abs(i - m2)
            return min(t1, t2)
        
        
