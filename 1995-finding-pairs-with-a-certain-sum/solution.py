class FindSumPairs(object):
    # freqmap for nums2
    # freqmap for nums1
    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums2 = nums2
        self.freq1 = defaultdict(int)
        self.freq2 = defaultdict(int)
        for n in nums1:
            self.freq1[n] += 1
        for n in nums2:
            self.freq2[n] += 1
            
        

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.freq2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.freq2[self.nums2[index]] += 1

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        cnt = 0
        for num in self.freq1:
            tgt = tot - num
            if tgt in self.freq2:
                cnt += self.freq1[num] * self.freq2[tgt]
        return cnt
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
