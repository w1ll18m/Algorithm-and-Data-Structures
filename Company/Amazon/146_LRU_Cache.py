class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nofitems = 0
        
        dummy_head = Node(-1, -1, None, None)
        dummy_tail = Node(-1, -1, dummy_head, None)
        dummy_head.next = dummy_tail
        self.head = dummy_head
        self.tail = dummy_tail

        self.cache = {}
    
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add_node(self, node):
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node 

    def get(self, key: int) -> int:
        # check if key exists in the cache
        if key not in self.cache:
            return -1

        # retrieve the node associated with the key
        node = self.cache[key]

        # remove the node from the linked list
        self.remove_node(node)

        # add the node to the end of the linked list
        self.add_node(node)    

        return node.val

    def put(self, key: int, value: int) -> None:
        # if the key exists then update its value
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove_node(node)
            self.add_node(node)
        
        # if the key does not exist and cache is not full then add it to the cache
        elif self.nofitems < self.capacity:
            node = Node(key, value, None, None)
            self.add_node(node)
            self.cache[key] = node
            self.nofitems += 1
        
        # if the key does not exist and cache is full then evict and add it to the cache
        else:
            lru = self.head.next
            self.cache.pop(lru.key)
            self.remove_node(lru)

            node = Node(key, value, None, None)
            self.add_node(node)
            self.cache[key] = node
        
'''
get(key) -> return the value of the key if it exists
put(key, value) -> update the value of the key if they key exists
    - evict the least recently used key

least recently used key (aka oldest element)
    - use dequeue? -> hard to extract elements from the middle
    - use a doubly linked list (keep track of start and end)

keep track of # of items in the cache using a counter variable

get -> use hashmap to map key to node
put -> use hashmap to check existance 
    - append to the end of the list (aka tail of the list)
    - to evict -> remove the head node (oldest)
updating recency -> find the node using map, remove node from list (using prev and next pointers), and append to the end of the list

thus total time complexity is O(1) and total space complexity is O(n) where n is the capacity
'''

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)