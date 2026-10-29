# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # def print_list(self, head):
    #     c = head
    #     output = []
    #     while c:
    #         output.append(c.val)
    #         c = c.next
    #     return output

    def reverseList(self, head):
        prev_node, curr_node = None, head

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        return prev_node

    def reorderList(self, head: Optional[ListNode]) -> None:
        c, length = head, 0
        while c:
            length += 1
            c = c.next
        
        c = head
        for i in range(math.ceil(length / 2) - 1):
            c = c.next
        second_half = c.next
        c.next = None
        first_half = head

        second_half = self.reverseList(second_half)    
        
        c1, c2 = first_half, second_half
        while c1:
            n1 = c1.next
            if c2:
                n2 = c2.next

            c1.next = c2
            c1 = n1
            if c2:
                c2.next = n1
                c2 = n2

# time: O(n)
# space: O(1)   


# the idea is: divide the linked list into two halves, first half is bigger or equal to second half
# reverse second half
# merge both by taking one node from each half each time