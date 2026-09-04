class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = []
        for letter in s:
            if letter == "*":
                stk.pop()
            else:
                stk.append(letter)
        return "".join(stk)
