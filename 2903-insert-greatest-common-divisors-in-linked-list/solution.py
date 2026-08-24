# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ok so need to insert new node with GCD value between every pair
        # whats algo for GCD of two ints a and b
        # euclidean
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        if head == None:
            return None
        tmp = head
        following = tmp.next
        while following != None:
            a = tmp.val
            b = following.val
            gcdVal = gcd(a, b)
            tmp.next = ListNode(gcdVal, following)
            following = following.next
            tmp = tmp.next.next
        return head
