class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.head = Node(-1)
        self.head.next = self.head
        self.head.prev = self.head
        self.size = 0
        self.k = k
        # just DLL with dummy node, last points to head

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.size == self.k:
            return False
        newNode = Node(value)
        nextNode = self.head.next

        self.head.next = newNode
        newNode.prev = self.head

        nextNode.prev = newNode
        newNode.next = nextNode

        self.size += 1
        return True


    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.size == self.k:
            return False
        newNode = Node(value)
        prevNode = self.head.prev

        self.head.prev = newNode
        newNode.next = self.head

        prevNode.next = newNode
        newNode.prev = prevNode

        self.size += 1
        return True
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.size == 0:
            return False
        
        nextNode = self.head.next.next

        self.head.next = nextNode
        nextNode.prev = self.head

        self.size -= 1
        return True
        

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.size == 0:
            return False
        
        nextNode = self.head.prev.prev
        
        self.head.prev = nextNode
        nextNode.next = self.head

        self.size -= 1
        return True
        

    def getFront(self):
        """
        :rtype: int
        """
        if self.size == 0:
            return -1
        return self.head.next.val
        

    def getRear(self):
        """
        :rtype: int
        """
        if self.size == 0:
            return -1
        return self.head.prev.val
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return (self.size == 0)
        

    def isFull(self):
        """
        :rtype: bool
        """
        return (self.size == self.k)


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
