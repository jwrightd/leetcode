class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        # js sldiing window for all size
        # wait no prefix sum maybe
        # then we get O(N * (r - l))
        maxSum = float('inf')
        N = len(nums)
        prefix = [0 for _ in range(N + 1)]
        prefix[1] = nums[0]
        for i in range(2, N + 1):
            prefix[i] = nums[i - 1] + prefix[i - 1]
        
        for left in range(N + 1):
            for right in range(left + l, left + r + 1):
                if right >= N + 1:
                    break
                if prefix[right] - prefix[left] > 0:
                    maxSum = min(maxSum, prefix[right] - prefix[left])





        return maxSum if maxSum != float('inf') else - 1
