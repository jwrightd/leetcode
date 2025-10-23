class Solution(object):
    def productExceptSelf(self, nums):
        #precompute prefix, suffix arrs
        n = len(nums)
        prefix_arr = [1] * n
        suffix_arr = [1] * n
        
        for i in range(1, n):
            prefix_arr[i] = (nums[i - 1] * prefix_arr[i - 1])
        
        for i in range(n - 2, -1, -1):
            suffix_arr[i] = (nums[i + 1] * suffix_arr[i + 1])
        outArr = []
        for i in range(0, n):
            outArr.append(prefix_arr[i] * suffix_arr[i])
        print(prefix_arr)
        print(suffix_arr)
        return outArr


        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
