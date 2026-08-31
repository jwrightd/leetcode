"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""

class Solution:
    def toArray(self, node):
        """
        :type head: Node
        :rtype: List[int]
        """
        # just go prev until beginning
        arr = []
        while node and node.prev:
            node = node.prev
        while node:
            arr.append(node.val)
            node = node.next
        return arr
