class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        #brute force is N^3
        # n^2 subarrays
        # summing their elements is n

        # but constraint is big, so maybe we can do in N
        # some sliding window thing potentially where we can expand and contract
        # but then you miss cases

        # prefix sum?
        # [1 0 5 3 6] 
        # can check pairs
        # if we subtract 3 - 0 (before arr), then we done
        # then can memo it, if we iterate on that array we have N^2
        
        # but if we put it into a dict and key what we would need
        # need --> highest idx of need
        # O(N) mem, O(N) time complex
        n = len(nums)
        prefixArr = [0] * n
        prefixArr[0] = nums[0]
        idx = 1
        while idx < n:
            prefixArr[idx] = nums[idx] + prefixArr[idx - 1]
            idx += 1
        maxSize = 0
        memo = {}
        #print(prefixArr)
        memo[0] = -1
        for idx, val in enumerate(prefixArr):
            # val - need = k
            need = val - k
            #print(need)
            if need in memo:
                maxSize = max(maxSize, idx - memo[need])

            if val not in memo:
                memo[val] = idx
        return maxSize
        

