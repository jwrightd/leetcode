# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None:
            return None
        last = head
        while last.next != None and last.next.next != None:
            last = last.next.next
        tmp = head
        adder = last
        while tmp != last:
            nextOdd = tmp.next.next
            evenNode = tmp.next
            endNode = adder.next
            adder.next = evenNode
            evenNode.next = endNode
            adder = adder.next
            tmp.next = nextOdd
            tmp = tmp.next
        

        return head

        
