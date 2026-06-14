# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        tmp = head
        count = 0
        while tmp != None:
            tmp = tmp.next
            count += 1
        arr = [0 for i in range(count//2)]
        for i in range(count//2):
            arr[i] = head.val
            head = head.next
        for i in range(count//2, count):
            arr[count - 1 - i] += head.val
            head = head.next
        return max(arr)
        
