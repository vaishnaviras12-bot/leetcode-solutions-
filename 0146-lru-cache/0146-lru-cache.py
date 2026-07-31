class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert (self,node):
        node.next = self.head.next
        node.prev= self.head

        self.head.next.prev=node
        self.head.next=node
    
        
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)
            return
        else:
            if self.capacity == len(self.cache):
               lru = self.tail.prev
               self.remove(lru)
               del self.cache[lru.key]
            new_node = Node(key,value)
            self.cache[key] = new_node
            self.insert(new_node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)