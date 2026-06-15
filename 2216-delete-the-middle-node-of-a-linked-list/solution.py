# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next == None:
            return None
        tmp = head
        count = 0
        while tmp != None:
            tmp = tmp.next
            count += 1
        
        nth = count//2
        tmp = head
        for i in range(nth - 1):
            tmp = tmp.next
        
        tmp.next = tmp.next.next
        return head
