# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        tmp = head
        if head == None:
            return None

        while tmp != None:
            vals.append(tmp.val)
            tmp = tmp.next
        vals.sort()
        N = len(vals)
        curr = 1
        newHead = ListNode(vals[0])
        tmp = newHead
        while curr < N:
            tmp.next = ListNode(vals[curr])
            tmp = tmp.next
            curr += 1
        return newHead
            
        
