"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        nodeDict = dict()
        nodeDict[None] = None
        tmp = head
        while tmp != None:
            nodeDict[tmp] = Node(tmp.val)
            tmp = tmp.next
        tmp = head
        copy = nodeDict[tmp]
        while tmp != None:
            copy.next = nodeDict[tmp.next]
            copy.random = nodeDict[tmp.random]
            copy = copy.next
            tmp = tmp.next
        return nodeDict[head]
            
        
