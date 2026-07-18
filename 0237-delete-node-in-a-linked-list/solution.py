# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # i am confused do we not just traverse and then skip?
        # oh we can't , so we just need to shift all values
        # algo:
        
        # if we have a next node:
        # take that value
        # replace current node with it
        # move to next node and repeat
        # if we do not have a next node
        
        # wait no, we want to check.next.next
        # if this is None, then we have one node next, we should take its value and then set our curr value to it and then set next ot be null
        while node.next.next != None:
            nextVal = node.next.val
            node.val = nextVal
            node = node.next
        node.val = node.next.val
        node.next = None
