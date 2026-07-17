class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # can obviously use dict to group by sum
        # but how to get two highest stuff
        # maybe max heap?
        import heapq

        grouping = {}
        currMax = -1

        def digitSum(i):
            dSum = 0
            while i > 0:
                dSum += i % 10
                i = i // 10
            return dSum
        
        for i in nums:
            dSum = digitSum(i)
            if dSum not in grouping:
                grouping[dSum] = i
            else:
                currMax = max(currMax, i + grouping[dSum])
                grouping[dSum] = max(grouping[dSum], i)
        

        return currMax

