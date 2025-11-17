# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head.next == None:
            return head if n == 0 else None
        numNodes = self.count(head)
        tmp = head
        for i in range(numNodes - 1 - n):
            tmp = tmp.next
        if numNodes - n == 0:
            return head.next
        tmp.next = tmp.next.next
        return head
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
    def count(self, head):
        return 1 + self.count(head.next) if head != None else 0
        
