class Solution(object):
    def generatePossibleNextMoves(self, currentState):
        """
        :type currentState: str
        :rtype: List[str]
        """
        res = []
        N = len(currentState)
        for i in range(N - 1):
            if currentState[i] == currentState[i + 1] == "+":
                change = currentState[:i] + "--" + currentState[i + 2:]
                res.append(change)
        return res
