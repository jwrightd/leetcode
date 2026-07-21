class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def convertToMin(time):
            hr = int(time[:2])
            minute = int(time[3:])
            totalMin = 60 * hr + minute
            return totalMin
        
        # brute force
        # check diff between all pairs
        # but we can do O(nlogn) i think if we just do sorting
        timePoints.sort()
        i = 0
        n = len(timePoints)
        minDiff = float('inf')
        while i < n - 1:
            first = timePoints[i]
            second = timePoints[i + 1]
            #print(convertToMin(second), convertToMin(first))
            minDiff = min(minDiff, convertToMin(second) - convertToMin(first), 24 * 60 - convertToMin(second) + convertToMin(first))
            #print(minDiff)
            i += 1
        #print(convertToMin(timePoints[0]), convertToMin(timePoints[n-1]))
        minDiff = min(minDiff, convertToMin(timePoints[n - 1]) - convertToMin(timePoints[0]), 24 * 60 - (convertToMin(timePoints[n - 1]) - convertToMin(timePoints[0])))
        return minDiff

        # connect back

        
