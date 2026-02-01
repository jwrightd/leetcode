# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heapify, heappop, heappush
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if lists == []:
            return None
        pq = []
        ret = ListNode()
        tmp = ret

        for idx, head in enumerate(lists):
            if head != None:
                heappush(pq, (head.val, idx, head))
        while len(pq) > 0:
            smallest = heappop(pq)
            v, idx, node = smallest
            tmp.next = ListNode()
            tmp = tmp.next
            tmp.val = v
            

            if node.next != None:
                heappush(pq, (node.next.val, idx, node.next))
        return ret.next


        
