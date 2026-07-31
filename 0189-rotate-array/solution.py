class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        newArr = [0] * N
        for idx, val in enumerate(nums):
            newArr[(idx + k) % N] = val
        for idx, val in enumerate(newArr):
            nums[idx] = newArr[idx]
        

