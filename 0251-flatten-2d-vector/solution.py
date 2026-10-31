class Vector2D(object):

    def __init__(self, vec):
        """
        :type vec: List[List[int]]
        """
        self.arr = []
        for arl in vec:
            for item in arl:
                self.arr.append(item)
        self.crt = 0
        

    def next(self):
        """
        :rtype: int
        """
        tmp = self.arr[self.crt]
        self.crt += 1
        return tmp

        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.crt < len(self.arr)
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
