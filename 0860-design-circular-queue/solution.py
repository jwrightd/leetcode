class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyCircularQueue(object):
    
    def __init__(self, k):
        """
        :type k: int
        """
        self.head = Node(-1)
        self.head.next = self.head
        self.last = self.head
        self.size = 0
        self.k = k
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.size == self.k:
            return False
        self.last.next = Node(value)
        self.last.next.next = self.head
        self.last = self.last.next
        self.size += 1
        return True
        
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.size == 0:
            return False
        if self.head.next == self.last:
            self.last = self.head
        self.head.next = self.head.next.next
        self.size -= 1
        return True

    def Front(self):
        """
        :rtype: int
        """
        return self.head.next.val
        

    def Rear(self):
        """
        :rtype: int
        """
        return self.last.val

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
