class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = []
        for ch in s:
            if ch != ")":
                stk.append(ch)
            else:
                rev = []
                while stk[-1] != "(":
                    rev.append(stk.pop(-1)[::-1])
                stk.pop(-1)
                stk.append("".join(rev))
        return "".join(stk)

        
