class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        #maybe prefix sum
        # 2 5 6 8 12 15
        # no not needed, can just do left and right two pointer
        left = 0
        right = 0
        total = 0
        N = len(nums)
        length = float('inf')
        for right in range(N):
            total += nums[right]
            #print(total)
            while total >= target:
                length = min(length, right - left + 1)
               # print(left, right)
                total -= nums[left]
                left += 1
        
        return length if length != float('inf') else 0
            

        
