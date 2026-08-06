# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        # need to get points to node before the part
        # node after the part
        before = None
        tmp = head
        position = 1
        if left == 1:
            before = None
        else:
            while position != left - 1:
                tmp = tmp.next
                position += 1
            before = tmp
        start = head if before == None else before.next
        while position != right:
            position += 1
            tmp = tmp.next
        end = tmp
        #print(start, end)
        while start != end:
            nextNode = end.next
            end.next = ListNode(start.val)
            end.next.next = nextNode
            start = start.next
        if before == None:
            return end
        else:
            before.next = end
        return head

        
