class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyHashSet:
    # array of listnodes
    def __init__(self):
        self.p = 11
        self.hs = [None for i in range(self.p)]

    def hasher(self, val):
        return val % self.p
    
    def add(self, key: int) -> None:
        bucket = self.hasher(key)
        #print(bucket)
        if self.hs[bucket] == None:
            self.hs[bucket] = Node(key)
        else:
            ptr = self.hs[bucket]
            while ptr.next != None and ptr.val != key:
                ptr = ptr.next
            if ptr.val != key:
                ptr.next = Node(key)

    def remove(self, key: int) -> None:
        bucket = self.hasher(key)
        ptr = self.hs[bucket]
        if ptr == None:
            return
        if ptr.val == key:
            self.hs[bucket] = ptr.next
        while ptr.next != None and ptr.next.val != key:
            ptr = ptr.next
        if ptr.next != None:
            ptr.next = ptr.next.next
    

    def contains(self, key: int) -> bool:
       # print()
        bucket = self.hasher(key)
        ptr = self.hs[bucket]
        
        if ptr == None:
            return False
        
        while ptr != None and ptr.val != key:
           # print(key, ptr.val)
            ptr = ptr.next
        
        if ptr != None:
           # print(key, ptr.val)
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
