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
        dummy = ListNode(-1, head)
        firstVal, lastVal = dummy.next, dummy.next
        while firstVal != None:
            while lastVal != None and lastVal.val == firstVal.val:
                lastVal = lastVal.next
            firstVal.next = lastVal
            firstVal = firstVal.next
            lastVal = firstVal
        return dummy.next


