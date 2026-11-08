class HitCounter(object):
    # bin search
    def __init__(self):
        self.arr = []

    def hit(self, timestamp):
        """
        :type timestamp: int
        :rtype: None
        """
        self.arr.append(timestamp)
        

    def getHits(self, timestamp):
        """
        :type timestamp: int
        :rtype: int
        """
        # bin search arr for smallest index that is current - 300
        tgt = timestamp - 300 + 1

        N = len(self.arr)
        l, r = 0, N - 1
        best = N
        while l <= r:
            mid = (l + r)//2
            if self.arr[mid] >= tgt:
                r = mid - 1
                best = mid
            else:
                l = mid + 1
                
        
        return len(self.arr) - best

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
