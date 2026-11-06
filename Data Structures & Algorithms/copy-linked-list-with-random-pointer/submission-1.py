"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def print_list(self, head):
        output = []
        c = head
        while c:
            if c.next and c.random:
                output.append((c, c.val, c.next.val, c.random.val))
            elif c.next and c.random is None:
                output.append((c, c.val, c.next.val, None))
            elif c.next is None and c.random:
                output.append((c, c.val, None, c.random.val))
            elif c.next is None and c.random is None:
                output.append((c, c.val, None, None))
            else:
                output.append('else')
            c = c.next
        return output

    # def print_original_to_copies(original_to_copies):
    #     my_dict = dict()
    #     for node in original_to_copies:
    #         my_dict(node.val) = original

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_to_copies = dict()
        res = c2 = Node(-1)

        c = head
        while c:
            c2.next = Node(c.val)

            c2 = c2.next
    
            original_to_copies[c] = c2
    
            c = c.next
    
        res = res.next
        
        # print(self.print_list(head))
        # print()
        # print()

        # print(self.print_list(res))
        # print(original_to_copies)
        # print()
        # print()


        for node in original_to_copies:
            copy_node = original_to_copies[node]
            
            node_random = node.random
            copy_node.random = original_to_copies[node_random] if node_random else None

            # original_to_copies[node].random = original_to_copies[node.random] if original_to_copies[node].random is not None else None
            # print(node, node_random, "     ", copy_node, node_random_copy)

        # print()
        # print(self.print_list(res))
        # print(original_to_copies)
        

        return res
