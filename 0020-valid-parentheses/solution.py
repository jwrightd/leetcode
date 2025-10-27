class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opens = "([{"
        closes = ")]}"
        elements = []
        for i in range(len(s)):
            if s[i] in opens:
                elements.append(s[i])
            elif s[i] in closes:
                if len(elements) == 0:
                    return False
                if closes[opens.index(elements[-1])] != s[i]:
                    return False
                else:
                    elements.pop()
        return len(elements) == 0
        
