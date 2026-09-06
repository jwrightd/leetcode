class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prod = 1
        N = len(nums)
        l = 0
        count = 0
        for r in range(N):
            prod *= nums[r]

            while prod >= k and l < N:
                prod //= nums[l]
                l += 1
            count += (r -l + 1)

        return count


        
