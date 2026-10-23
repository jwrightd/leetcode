# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # easy to just do n-k, still same magnitude
        if head == None:
            return None
        if head.next == None:
            return head
        N = 1
        last = head
        while last.next != None:
            last = last.next
            N += 1
        tgt = N - k % N
        for i in range(tgt):
            nxt = head.next
            head.next = None
            last.next = head
            last = last.next
            head = nxt
        return head
            

        

        
