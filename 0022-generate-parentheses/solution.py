class Solution(object):
    arr = []
    def generateParenthesis(self, n):
        self.arr = []
        self.recur(n, 0, 0, "")
        return self.arr
        """
        :type n: int
        :rtype: List[str]
        """
    def recur(self, n, closed, op, st):
        if closed + op == 2 *n:
            self.arr.append(st)
            #print(st)
        if closed < n:
            self.recur(n, closed + 1, op, st + "(")
        if op < closed:
            self.recur(n, closed, op + 1, st + ")")
        
        
