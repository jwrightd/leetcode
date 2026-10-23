# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: List[Optional[ListNode]]
        """

        res = []
        tmp = head
        N = 0
        while tmp != None:
            tmp = tmp.next
            N += 1
        for i in range(k):
            size = N // (k - i) + 1 if N % (k - i) != 0 else N // (k - i)
            dummy = ListNode(-1)
            res.append(dummy)
            tmp = dummy
            for _ in range(size):
                tmp.next = head
                tmp = tmp.next
                head = head.next
            tmp.next = None
            res[i] = res[i].next
            N -= size
        return res


        
