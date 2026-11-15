class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        :type maxNumbers: int
        """
        # maybe can do hashmap implementation with size var
        self.map = {}
        self.size = maxNumbers
        self.unused = []
        for i in range(maxNumbers):
            self.unused.append(i)
        

    def get(self):
        """
        :rtype: int
        """
        # just pop-1 for o(1) tc
        if len(self.unused) > 0:
            tgt = self.unused.pop(-1)
            self.map[tgt] = 1 # 1 is used, 0 free
            return tgt
        else:
            return -1

        

    def check(self, number):
        """
        :type number: int
        :rtype: bool
        """
        return (number in self.map and self.map[number] == 0) or number not in self.map

    def release(self, number):
        """
        :type number: int
        :rtype: None
        """
        if number in self.map and self.map[number] == 1:
            self.map[number] = 0
            self.unused.append(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
