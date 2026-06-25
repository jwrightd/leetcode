class Node(object):
    def __init__(self, key=0, value=0):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value

class LRUCache(object):
    # KV dictionary for o(1) access
    # can do get and put with KV dict, but we have capacity
    # how to do LRU? we need to track the order of calls
    # not list, we use DLL for tracking our nodes, hashmap to access them in O(1)

    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node()
        self.head.next = self.head
        self.head.prev = self.head
        #dummy node
        self.size = 0
        self.cache = dict() # key --> node

        """
        :type capacity: int
        """
        

    def get(self, key):
        # need to move to front of DLL
        if key not in self.cache:
            return -1
        target = self.cache[key]

        prevNode = target.prev
        nextNode = target.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

        nextHead = self.head.next
        self.head.next = target
        target.next = nextHead
        nextHead.prev = target
        target.prev = self.head
        return target.value

        """
        :type key: int
        :rtype: int
        """
        

    def put(self, key, value):
        # we are going to add or update then
        # remove last if size > cap
        if key in self.cache:
            target = self.cache[key]

            prevNode = target.prev
            nextNode = target.next
            
            prevNode.next = nextNode
            nextNode.prev = prevNode

            nextHead = self.head.next
            self.head.next = target
            target.next = nextHead
            nextHead.prev = target
            target.prev = self.head

            self.cache[key].value = value
        else:
            self.cache[key] = Node(key, value) #update DLL
            tmp = self.head.next
            self.head.next = self.cache[key]
            self.cache[key].next = tmp
            self.cache[key].prev = self.head
            tmp.prev = self.cache[key]
            self.size += 1
            if self.size > self.capacity: #LRU, remove last node
                victim = self.head.prev
                newLast = self.head.prev.prev
                newLast.next = self.head
                self.head.prev = newLast
                del self.cache[victim.key]




        """
        :type key: int
        :type value: int
        :rtype: None
        """
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
