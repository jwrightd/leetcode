# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        stuff = set()
        tmp = headA
        while tmp != None:
            stuff.add(tmp)
            tmp = tmp.next
        tmp = headB
        while tmp != None:
            if tmp in stuff:
                return tmp
            tmp = tmp.next
        return None
        
