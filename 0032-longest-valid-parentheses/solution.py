class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        #)(()
        # ok we have a current count and a global count
        # if we pop, current count += 2, update global
        # if we hit a ) and stk is empty, reset stack and current count = 0
        global_cnt = 0
        stk = [-1]
        for idx, ch in enumerate(s):
            if ch == "(":
                stk.append(idx)
            else: # ) case
                stk.pop(-1)

                if len(stk) == 0: # then we popped the boundary
                    stk.append(idx)
                else:
                    global_cnt = max(global_cnt, idx - stk[-1])
        return global_cnt
