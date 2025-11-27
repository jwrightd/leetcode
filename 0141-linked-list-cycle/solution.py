# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head == None: 
            return False
        p1 = head
        p2 = head.next
        while p1 != p2 and p2 != None and p2.next != None:
            p2 = p2.next.next
            p1 = p1.next
        return p2 == p1
        """
        :type head: ListNode
        :rtype: bool
        """
        
