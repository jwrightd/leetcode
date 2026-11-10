class Solution(object):
    def canWin(self, currentState):
        """
        :type currentState: str
        :rtype: bool
        """
        def moves(currentState):
            res = []
            N = len(currentState)
            for i in range(N - 1):
                if currentState[i] == currentState[i + 1] == "+":
                    change = currentState[:i] + "--" + currentState[i + 2:]
                    res.append(change)
            return res
        
        visited = {}
        def dfs(state):
            if state in visited:
                return visited[state]
            nextMoves = moves(state)
            if len(nextMoves) == 0:
                return False
            for nextState in nextMoves:
                if not dfs(nextState):
                    visited[state] = True
                    return True
            visited[state] = False
            return False
        return dfs(currentState)

