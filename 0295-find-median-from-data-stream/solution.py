class MedianFinder(object):
    # i think we keep a num for size
    def __init__(self):
        self.size = 0
        self.nums = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        tmp = self.size
        l, r = 0, self.size - 1
        mid = (l + r)//2

        while l <= r: # invariant is [l ,h]
            if self.nums[mid] == num:
                self.nums.insert(mid + 1, num)
                self.size += 1
                break
            if self.nums[mid] > num:
                r = mid - 1
            else:
                l = mid + 1
            mid = (l + r)//2

        if tmp == self.size:
            self.nums.insert(mid + 1, num)
            self.size += 1
        # bst to add
        

    def findMedian(self):

        """
        :rtype: float
        """
        if self.size % 2 == 0: # even
            medIdx = self.size//2 - 1
            return float(self.nums[medIdx] + self.nums[medIdx + 1])/2
        else:
            return self.nums[self.size//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
