class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:
    # def print_all(self):
    #     c = self.lru
    #     output = []
    #     while c:
    #         output.append(c.key)
    #         c = c.next
    #     print(output, self.cache)


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
        # print("get", key)
        # self.print_all()
        if key not in self.cache:
            # self.print_all()
            return -1
        node = self.cache[key]
        self.remove_node(node)
        self.insert_node(node)
        # self.print_all()
        return node.val

    def put(self, key: int, value: int) -> None:
        # print("put", key, value)
        # self.print_all()
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            node.val = value
            self.insert_node(node)
        else:
            # print("here")
            new_node = Node(key, value)
            self.cache[key] = new_node
            # self.print_all()
            self.insert_node(new_node)
            # self.print_all()
            if len(self.cache) > self.capacity:
                # self.print_all()
                lru_node = self.lru.next 
                del self.cache[lru_node.key]
                self.remove_node(lru_node)
                # self.print_all()
        # self.print_all()
