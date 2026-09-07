class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # do arr of max, arr of min
        N = len(nums)
        maxVals = [0 for _ in range(N)]
        minVals = [0 for _ in range(N)]
        maxN = float('-inf')
        for idx, val in enumerate(nums):
            maxN = max(maxN, val)
            maxVals[idx] = maxN
        minN = float('inf')
        for i in range(N - 1, -1, -1):
            minN = min(minN, nums[i])
            minVals[i] = minN
        for i in range(N):
            if maxVals[i] - minVals[i] <= k:
                return i
        return -1
        
