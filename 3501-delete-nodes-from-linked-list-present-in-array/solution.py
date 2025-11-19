# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        if head == None:
            return None
        numSet = set()
        for i in nums:
            numSet.add(i)
        while head.val in numSet:
            head = head.next
        tmp = head
        while tmp != None and tmp.next != None:
            if tmp.next.val in numSet:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return head
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
