# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        return self.recur(l1, l2, 0)

    def recur(self, l1, l2, num):
        if l1 == None and l2 == None:
            return None if num == 0 else ListNode(num, None)
        elif l1 == None:
            if num == 0:
                return l2
            else:
                total = l2.val + 1
                return ListNode(total % 10, self.recur(None, l2.next, total//10))
        elif l2 == None:
            if num == 0:
                return l1
            else:
                total = l1.val + 1
                return ListNode(total % 10, self.recur(l1.next, None, total//10))
        else:
            totalInfo = l1.val + l2.val + num
            if totalInfo >= 10:  
                return ListNode(totalInfo % 10, self.recur(l1.next, l2.next, totalInfo//10))
            else:
                return ListNode(totalInfo, self.recur(l1.next, l2.next, 0))

            
