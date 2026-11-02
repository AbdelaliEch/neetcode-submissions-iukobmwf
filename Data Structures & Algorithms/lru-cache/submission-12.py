class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = None
        self.prev = None

class LRUCache:
    def print_list(self, head):
        c = head
        output = []
        while c:
            output.append((c.key))
            c = c.next
        return output

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.cache = dict()
        self.lru, self.mru = Node(-1, -1), Node(-1, -1)
        self.lru.next, self.mru.prev = self.mru, self.lru

    def remove_node(self, node, del_from_cache: bool):
        prv, nxt = node.prev, node.next
        nxt.prev, prv.next = prv, nxt
        if del_from_cache:
            del self.cache[node.key]
        self.length -= 1


    def insert_node(self, node):
        last_node = self.mru.prev
        last_node.next = node
        node.next, node.prev = self.mru, last_node
        self.mru.prev = node
        self.length += 1
        if self.length > self.capacity:
            self.remove_node(self.lru.next, True)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove_node(self.cache[key], False)
        self.insert_node(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update cache value, remove and insert node at the front without deleting node from cache
            self.cache[key].val = value
            self.remove_node(self.cache[key], False)
            self.insert_node(self.cache[key])
        else:
            # insert node at the front
            self.cache[key] = Node(key, value)
            self.insert_node(self.cache[key])


# to remember the nodes, make the dict map each key to its node, instead of key:value, use key:node