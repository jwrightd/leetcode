class FreqStack(object):
    import heapq
    def __init__(self):
        self.freq = defaultdict(int)
        self.stacks = defaultdict(list)
        self.heap = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.freq[val] += 1
        self.stacks[self.freq[val]].append(val)
        heapq.heappush(self.heap, [-self.freq[val], val])


        

    def pop(self):
        """
        :rtype: int
        """
        negFreq, val = heapq.heappop(self.heap)

        #print(maxKey, maxVal)
        #print(self.freq)
        #print(self.stacks)
        res = self.stacks[-negFreq].pop(-1)
        self.freq[val] -= 1

        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
