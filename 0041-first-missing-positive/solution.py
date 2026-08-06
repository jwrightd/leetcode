class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        for i in range(N):
            idx = i
            while 1 <= nums[idx] <= N and nums[nums[idx] - 1] != nums[idx]:
                tmp = nums[nums[idx] - 1]
                nums[nums[idx] - 1] = nums[idx]
                nums[idx] = tmp
                #idx
            
        #print(nums)
        count = 1
        for i in nums:
            if i != count:
                return count
            count += 1
        return N + 1
        
        # oh i see, we sum up the positive ints
        # check the num of them
        
