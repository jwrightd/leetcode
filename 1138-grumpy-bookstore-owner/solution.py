class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        # sliding window
        base = 0
        N = len(customers)
        for i in range(N):
            if grumpy[i] == 0:
                base += customers[i]
                customers[i] = 0
           # else:
                
        # now sliding window for max
        windowSum = 0
        for i in range(minutes):
            windowSum += customers[i]
        maxSum = windowSum
        for right in range(minutes, N):
            windowSum += customers[right]
            windowSum -= customers[right - minutes]
            maxSum = max(windowSum, maxSum)
        return base + maxSum

