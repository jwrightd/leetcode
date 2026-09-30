class RandomizedSet(object):
    import random
    def __init__(self):
        # set can have o1 insert, remove
        # how do we do random?
        # maybe we can just do random library
        # but then we need arr
        # ok so we have arr
        # insert is O1 to end
        # but then remove is o(N)
        # but we can hashmap to the right, swap to end, and then remove in O(1)
        self.arr = []
        self.indices = {}


    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.indices:
            return False
        size = len(self.arr)
        self.indices[val] = size
        self.arr.append(val)
        return True # O(1)


    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """

        # okay a few steps here
        # first check if val in randomset
        if val not in self.indices:
            return False
        # then if it is in, we need to swap to back
        tgtIdx = self.indices[val]
        last = len(self.arr) - 1
        lastVal = self.arr[last]
        self.arr[tgtIdx], self.arr[last] = lastVal, val
        # then we need to edit indices
        self.indices[val], self.indices[lastVal] = last, tgtIdx
        self.indices.pop(val)
        self.arr.pop(-1)
        return True


        

    def getRandom(self):
        #print(self.arr)
        return self.arr[random.randint(1, len(self.arr)) - 1] # o1

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
