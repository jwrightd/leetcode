class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque
        # init might seem like graph problem
        # i think it is
        # minimum num of total turns --> BFS
        # ok so let's just set this algorithm:
        # we BFS starting at 0, target is our target
        # prune dead ends
        deadSet = set(deadends)
        visited = set()
        queue = deque([["0000", 0]]) # node, numTurns

        def getChildren(node):
            children = []
            for i in range(4):
                val = int(node[i])
                possible = [str((val + 1) %10), str((val - 1) % 10)]
                children.append(node[:i] +possible[0] + node[i + 1:])
                children.append(node[:i] +possible[1] + node[i + 1:])
            return children

        while queue:
            node, numTurns = queue.popleft()
            if node in visited or node in deadSet:
                continue
            
            if node == target:
                return numTurns
            visited.add(node)
            # children of a current node are each slot +- 1
            # might want to consider doing this in smart way instead of creating new strings each time
            for neighbor in getChildren(node):
                queue.append([neighbor, numTurns + 1])
        
        return -1



