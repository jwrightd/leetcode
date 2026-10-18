# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        if head == None:
            return None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: # cycle found
                break
        
        if slow != fast or head.next == None or head.next.next == None: # no cycle
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast
        
