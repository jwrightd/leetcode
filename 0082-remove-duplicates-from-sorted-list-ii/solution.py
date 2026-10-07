# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # two ptr
        if head == None:
            return None
        dummy = ListNode(0, head)
        prev = dummy
        while head:
            if head.next != None and head.next.val == head.val:
                while head.next != None and head.next.val == head.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return dummy.next
        
