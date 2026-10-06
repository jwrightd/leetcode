class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stk = [0]
        for ch in s:
            if ch == "(":
                stk.append(0)
            else:
                score = stk.pop(-1)
                stk[-1] += max(2 * score, 1)
        


                

            

        return stk[0]

