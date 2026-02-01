class Solution(object):
     
    def climbStairs(self, n):
        table =[-1 for i in range(n)]
        return self.recur(n, table)

    def recur(self, n, table):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if table[n - 1] != -1:
            return table[n - 1]
        num = self.recur(n - 2, table) + self.recur(n - 1, table)
        table[n - 1] = num
        return num


# 1 - 1
# 2 - 2
# 3 - 3
# 4 - 5
