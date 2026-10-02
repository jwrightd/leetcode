class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        def recur(crnt, i):
            if i == N:
                return 0
            
            cnt = crnt
            for k in range(i + 1, N):
                cnt += recur(crnt ^ nums[k], k)
            return cnt
        runSum = 0
        for i in range(N):
            runSum += recur(nums[i], i)
        return runSum
