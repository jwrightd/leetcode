# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        count = 0
        ptr = head

        while ptr != None and ptr.next != None:
            print(count)
            ptr = ptr.next
            count += 1
        for i in range(count):
            ptr.next = ListNode(head.val, ptr.next)
            head = head.next
        return head
