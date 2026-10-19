# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        smaller = ListNode(-101)
        bigger = ListNode(-101)

        s_tmp = smaller
        b_tmp = bigger
        while head != None:
            if head.val < x:
                s_tmp.next = head
                s_tmp = s_tmp.next
            else:
                b_tmp.next = head
                b_tmp = b_tmp.next
            head = head.next

        b_tmp.next = None
        smallList = smaller.next
        bigList = bigger.next

        if smallList == None:
            return bigList
        s_tmp.next = bigList

        return smallList
        
