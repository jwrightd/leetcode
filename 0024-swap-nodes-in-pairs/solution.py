# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #.swap first two and recur
        # first check the number of nodes
        # if 0, return None
        # if 1, return that node
        # if >= 2 then do algo
        if head == None:
            return None
        if head.next == None:
            return head
        
        nextPair = head.next.next
        
        nextNode = head.next
        nextNode.next = head
        head.next = self.swapPairs(nextPair)
        return nextNode
