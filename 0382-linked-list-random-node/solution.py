# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        # probably want getrandom to be o1
        # so maybe hashmap to index
        self.head = head
        self.map = {}
        size = 0
        tmp = head
        while tmp != None:
            self.map[size] = tmp
            size += 1
            tmp = tmp.next
        self.size = size
        

    def getRandom(self):
        """
        :rtype: int
        """
        return self.map[random.randint(0, self.size - 1)].val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
