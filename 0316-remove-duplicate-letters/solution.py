class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # can do monotonically inc stack
        # need some way to track if there are future occurrences
        # and then a set to see whats on the stack

        stk = []
        lastIdx = {}
        used = set()

        N = len(s)

        for idx, val in enumerate(s):
            lastIdx[val] = idx
        
        for idx, val in enumerate(s):
            if val not in used:
                while stk and stk[-1] > val and lastIdx[stk[-1]] > idx:
                    used.remove(stk.pop(-1))
                
                stk.append(val)
                used.add(val)
        return "".join(stk)
