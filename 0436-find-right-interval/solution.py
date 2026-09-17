class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        N = len(intervals)
        # for every item in intervals, we want to find the smallest idx where start is bigger than the end
        output = [0 for _ in range(N)]
        idxMap = {}
        for idx, val in enumerate(intervals):
            idxMap[tuple(val)] = idx
        
        intervals.sort()

        for idx, val in enumerate(intervals):
            start, end = val
            lower, upper = idx, N - 1
            
            best = -1
            while lower <= upper:
                mid = (lower + upper)//2
                if intervals[mid][0] >= end:
                    best = mid
                    upper = mid - 1
                else:
                    lower = mid + 1
            output[idxMap[tuple(val)]] = idxMap[tuple(intervals[best])] if best != -1 else -1
        return output

            

