class TimeMap(object):

    def __init__(self):
        # we can maybe do dict with key --> tuple amd dict with key --> max
        self.kvPair = {}
        self.kTime = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.kvPair[(key, timestamp)] = value
        if key not in self.kTime:
            self.kTime[key] = []
        self.kTime[key].append(timestamp)

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.kTime:
            return ""
        
        #binary search
        times = self.kTime[key]
        best = -1 # want greatest timestamp <= timestamp
        left = 0
        right = len(times) - 1
        mid = (left + right)//2

        while left <= right:
            mid = (left + right) // 2

            if times[mid] <= timestamp:
                best = mid
                left = mid + 1
            else:
                right = mid - 1

        if best == -1:
            return ""

        return self.kvPair[(key, times[best])]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
