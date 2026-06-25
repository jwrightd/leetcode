class MinStack(object):

    def __init__(self):
        # what if our stack is just tuples, (val, curr_min)
        self.stk = []
        self.curr_min = float('inf')

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.curr_min = min(self.curr_min, value)
        self.stk.append((value, self.curr_min))
        

    def pop(self):
        self.stk.pop(-1)
        if self.stk:
            peek = self.stk[-1] #new top of stk
            val, newMin = peek
            self.curr_min = newMin
        else:
            self.curr_min = float('inf')

        

    def top(self):
        val, minimum = self.stk[-1]
        return val
        

    def getMin(self):
        return self.curr_min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
