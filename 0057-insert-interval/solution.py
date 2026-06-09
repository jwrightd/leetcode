class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        #algorithm
        if intervals == []:
            return [newInterval]
        # make new list
        output = []

        # add intervals until current interval end is less than the newinterval start
        count = 0
        while count < len(intervals) and intervals[count][1] < newInterval[0]:
            output.append(intervals[count])
            count += 1
        if count < len(intervals):
        # create a new interval with start of new interval
            if newInterval[1] < intervals[count][0]:
                start, end = newInterval
            else:   
                start = min(intervals[count][0], newInterval[0])
                end = max(intervals[count][1], newInterval[1])
        else:
            start, end = newInterval
        
        # continue going on intervals until end of new interval < start of next interval
        while count < len(intervals) and end > intervals[count][1]:
            count += 1
        
        if count < len(intervals) and intervals[count][0] <= end:
            end = intervals[count][1]
            count += 1
        
        output.append([start, end])

        # add [start, end]
        while count < len(intervals):
            output.append(intervals[count])
            count += 1
        #add rest of stuff
        return output
        
