# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # just stack monotonic decreasing
        stk = []
        while head:
            while stk and stk[-1].val < head.val:
                stk.pop(-1)
            stk.append(head)
            head = head.next
        N = len(stk)
        for i in range(N - 1):
            stk[i].next = stk[i + 1]
        return stk[0]


