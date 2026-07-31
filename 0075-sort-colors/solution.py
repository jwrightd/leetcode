class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]
        for i in nums:
            counts[i] += 1
        N = len(nums)
        counts[1] += counts[0]
        counts[2] += counts[1]
        # prefxi sum
        for i in range(0, counts[0]):
            nums[i] = 0
        for i in range(counts[0], counts[1]):
            nums[i] = 1
        for i in range(counts[1], N):
            nums[i] = 2
        
        
