class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        #just dictionary, then can divide by balloon count
        balloons = dict()
        bloon = "balon"
        for i in bloon:
            balloons[i] = 0
        for i in text:
            if i in bloon:
                balloons[i] += 1
        return min([balloons[i]//"balloon".count(i) for i in balloons])
