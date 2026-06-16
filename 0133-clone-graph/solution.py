"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        #whats best algo for this?
        #maybe like BFS we do layer by layer?
        # so let's do this:
        #we have a queue, we add add neighbors into queuewwww
        if node == None:
            return None

        nodeDict = dict()
        nodeDict[node.val] = Node(node.val)

        q = [node]
        while q:
            curr = q.pop(0)
            for n in curr.neighbors:
                if n.val not in nodeDict:
                    q.append(n)
                    nodeDict[n.val] = Node(n.val)
                nodeDict[curr.val].neighbors.append(nodeDict[n.val])
        return nodeDict[node.val]


