class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.lru, self.mru = Node(-1, -1), Node(-1, -1)
        self.lru.next, self.mru.prev = self.mru, self.lru

    def remove_node(self, node, del_from_cache: bool):
        prv, nxt = node.prev, node.next
        nxt.prev, prv.next = prv, nxt
        if del_from_cache:
            del self.cache[node.key]

    def insert_node(self, node):
        last_node = self.mru.prev
        last_node.next = node
        node.next, node.prev = self.mru, last_node
        self.mru.prev = node
        if len(self.cache) > self.capacity:
            self.remove_node(self.lru.next, True)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_node(node, False)
        self.insert_node(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]        
            node.val = value
            self.remove_node(node, False)
            self.insert_node(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert_node(node)

# O(1) time
