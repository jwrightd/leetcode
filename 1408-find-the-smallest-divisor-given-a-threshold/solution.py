class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def getDivSum(k):
            tot = 0
            for i in nums:
                tot += (i//k if i % k == 0 else i //k + 1)
            return tot
        
        lower, higher = 1, max(nums)
        best = higher

        while lower <= higher:
            mid = (lower + higher)//2
            result = getDivSum(mid)
            if result <= threshold:
                best = mid
                higher = mid - 1
            else:
                lower = mid + 1
        return best

        
