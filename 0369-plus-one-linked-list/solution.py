# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def algo(head):
            if head == None:
                return None, 0
            toAdd = 0
            if head.next == None:
                if head.val == 9:
                    head.val = 0
                    toAdd = 1
                else:
                    head.val += 1
                return head, toAdd
            rest, add = algo(head.next)

            nextAdd = 0
            head.next = rest
            head.val += add
            if head.val == 10:
                head.val = 0
                nextAdd = 1



            return head, nextAdd
        node, add = algo(head)
        if add == 1:
            newHead = ListNode(1, node)
            return newHead
        return node
