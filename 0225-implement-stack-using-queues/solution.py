class MyStack(object):

    def __init__(self):
        self.main = []
        self.helper = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.helper.append(x)
        while self.main:
            self.helper.append(self.main.pop(0))
        self.main = self.helper
        self.helper = []
        

    def pop(self):
        """
        :rtype: int
        """
        return self.main.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        return self.main[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.main) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
