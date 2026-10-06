class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        moves = 0
        for ch in s:
            if ch == "(":
                counter += 1
            else:
                counter -= 1
            if counter < 0:
                moves += 1
                counter = 0
        return moves + counter

