class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru, self.mru = Node(0, 0), Node(0, 0)
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def insert_node(self, node):
        last_cache_node = self.mru.prev
        last_cache_node.next = self.mru.prev = node
        node.next = self.mru
        node.prev = last_cache_node

    def remove_node(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove_node(self.cache[key])
            self.insert_node(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert_node(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.lru.next
            self.remove_node(lru)
            del self.cache[lru.key]

# time: 
# space: 