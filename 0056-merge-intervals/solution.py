class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        ret = []
        count = 0
        for i in intervals:
            if i[0] <= end:
                end = max(i[1], end)
            else:
                ret.append([start, end])
                start = i[0]
                end = i[1]
            count += 1
            if count == len(intervals):
                ret.append([start, end])
        return ret
        
