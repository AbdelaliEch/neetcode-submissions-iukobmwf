class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict() 
        self.lru, self.mru = Node(-1, -1), Node(-1, -1)
        self.lru.next, self.mru.prev = self.mru, self.lru

    def remove_node(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def insert_node(self, node):
        last_node = self.mru.prev
        node.prev, node.next = last_node, self.mru
        self.mru.prev = last_node.next = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_node(node)
        self.insert_node(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            node.val = value
            self.insert_node(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.insert_node(new_node)
            if len(self.cache) > self.capacity:
                lru_node = self.lru.next 
                del self.cache[lru_node.key]
                self.remove_node(lru_node)
