class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None
        self.use = 1

class DLL:
    def __init__(self):
        self.dummy_head = Node(-1, -1)
        self.dummy_tail = Node(-1, -1)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        
class LFUCache(object):
    def __init__(self, capacity):
        '''
        so first we have standardhasmap KV, key is given key, value is node we create with the value stored. then freqmap is freq int to DLL, we write DLL and ndoe classes. 

        then we have a global ptr for lowest frequency that we maintain

        when we reach capacity in the hashmap, we need to pop something from the lowestg freq, this must be the head of the DLL

        whenever we do get, we can o1 access the node and redraw the connection to put the node at the end of freq+1
        '''
        self.minFreq = 0
        self.freqMap = {}
        self.kV = {}
        self.capacity = capacity
        self.freqMap[0] = DLL()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.kV:
            val = self.kV[key]

            prevNode = val.prev
            nextNode = val.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            
            if self.freqMap[val.use].dummy_head.next == self.freqMap[val.use].dummy_tail and self.minFreq == val.use:
                self.minFreq += 1
            val.use += 1
            if val.use not in self.freqMap:
                self.freqMap[val.use] = DLL()
            newPrev = self.freqMap[val.use].dummy_tail.prev
            newPrev.next = val
            val.next = self.freqMap[val.use].dummy_tail
            val.prev = newPrev
            self.freqMap[val.use].dummy_tail.prev = val
            return val.val
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.kV:
            val = self.kV[key]
            val.val = value

            prevNode = val.prev
            nextNode = val.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            if self.freqMap[val.use].dummy_head.next == self.freqMap[val.use].dummy_tail and self.minFreq == val.use:
                self.minFreq += 1
            val.use += 1
            if val.use not in self.freqMap:
                self.freqMap[val.use] = DLL()
            newPrev = self.freqMap[val.use].dummy_tail.prev
            newPrev.next = val
            val.next = self.freqMap[val.use].dummy_tail
            val.prev = newPrev
            self.freqMap[val.use].dummy_tail.prev = val
        else:
            if len(self.kV) == self.capacity:
                deleted = self.freqMap[self.minFreq].dummy_head.next
                self.freqMap[self.minFreq].dummy_head.next = deleted.next
                deleted.next.prev = self.freqMap[self.minFreq].dummy_head
                del self.kV[deleted.key]
            self.minFreq = 1
            self.kV[key] = Node(key, value)
            # add
            val = self.kV[key]
            if 1 not in self.freqMap:
                self.freqMap[1] = DLL()
            newPrev = self.freqMap[1].dummy_tail.prev
            newPrev.next = val
            val.next = self.freqMap[1].dummy_tail
            val.prev = newPrev
            self.freqMap[1].dummy_tail.prev = val

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
