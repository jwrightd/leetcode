# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        #idea: dict of nodes by idx so we have o(1) retrieval after o(N) pass
        #build up list with pattern

        nodeDict = dict()
        tmp = head
        count = 0
        while tmp != None:
            nodeDict[count] = tmp
            tmp = tmp.next
            count += 1
        
        #now we build
        left = 0
        right = count - 1
        while right > left:
            nodeDict[left].next = nodeDict[right]
            nodeDict[right].next = nodeDict[left + 1]
            left += 1
            right -= 1
        nodeDict[left].next = None
        return nodeDict[0]
        
