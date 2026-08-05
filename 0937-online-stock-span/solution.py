class StockSpanner(object):

    def __init__(self):
        self.stk = []
        

    def next(self, price):
        output = 1
        while self.stk and self.stk[-1][0] <= price:
            output += self.stk[-1][1]
            self.stk.pop(-1)
            
        self.stk.append((price, output))
        return output
        """
        :type price: int
        :rtype: int
        """
        
# want to store (val, span)
# 28, 1
# 14, 1
# 28

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


# need to be able to find the last num bigger than price
