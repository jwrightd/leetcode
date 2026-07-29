class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arrIdx = 0
        currIdx = 0
        k = 0
        N = len(nums)
        while currIdx < N:
            if nums[currIdx] != val:
                nums[arrIdx] = nums[currIdx]
                arrIdx += 1
            else:
                k += 1
            currIdx += 1
        return N - k
            
