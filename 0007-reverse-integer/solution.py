class Solution(object):
    def reverse(self, x):
        negative = (x < 0)
        x = -x if negative else x
        stk = []
        while x > 0:
            stk.append(x%10)
            x = (x-x%10)/10
        count = 0
        rev = 0
        limit = 2147483647
        while len(stk) > 0:
            tmp = stk.pop()
            #len num = count + 1
            if count > 9:
                return 0
            if count == 9 and tmp > 2:
                return 0
            if count == 9 and tmp >= 2 and rev > 147483647:
                return 0
            rev += tmp * 10 ** count
            count += 1
        # use q
        # 321 --> 1 | 2 | 3
        return -rev if negative else rev
        
        
