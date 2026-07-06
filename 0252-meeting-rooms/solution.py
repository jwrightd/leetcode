class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        n = len(intervals)
        if n <= 1:
            return True
        # just check over intervals to see if overlap
        sortedIntervals = sorted(intervals)

        idx = 0
        
        while idx < n - 1:
            if sortedIntervals[idx][1] > sortedIntervals[idx + 1][0]: #overlap
                return False
            idx += 1
        return True

