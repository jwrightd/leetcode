# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        return self.recur(head, k)
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
    def recur(self, head, k):
        if not self.hasK(head, k):
            return head
        tmp = head
        for i in range(k - 1):
            tmp = tmp.next #at end, tmp points at last node in group
        nextGroup = tmp.next
        while head != tmp:
            end = tmp.next
            tmp.next = head
            nextNode = head.next
            head.next = end
            head = nextNode
        last = head
        for i in range(k - 1):
            last = last.next
        last.next = self.recur(nextGroup, k)
        return head
            



    def hasK(self, head, k):
        if head == None:
            return False
        count = 1
        while (head.next != None):
            count += 1
            head = head.next
        return count >= k
        
