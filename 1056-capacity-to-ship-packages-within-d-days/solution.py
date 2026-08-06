class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        # bin search
        # capacity low is 1
        # high is max(weight)
        low = max(weights)
        high = (max(weights)) * len(weights)
        mid = (low + high)//2
        best = high
        #print(high)


        def working(capacity):
            currDay = 0
            runSum = 0
            for i in weights:
                if runSum + i > capacity:
                    currDay += 1
                    runSum = i
                else:
                    runSum += i
            return currDay < days
        #print(work)
        while low <= high:
            mid = (low + high)//2
            if working(mid):
                best = min(best, mid)
                high = mid - 1
            else:
                low = mid + 1
        return best

