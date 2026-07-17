class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minDist = float('inf')
        def reverseNum(i):
            rNum = 0
            stk = []
            while i > 0:
                stk.append(i % 10)
                i = i // 10
            pwr = 0
            while stk:
                rNum += stk.pop() * 10 ** pwr
                pwr += 1
            return rNum
        
        revDict = {}
        for idx, val in enumerate(nums):

            reversedNum = reverseNum(val)
            if val in revDict:
                minDist = min(minDist, abs(idx - revDict[val]))
            # maybe we just store the num without 0s at end
            revDict[reversedNum] = idx
        return -1 if minDist == float('inf') else minDist
