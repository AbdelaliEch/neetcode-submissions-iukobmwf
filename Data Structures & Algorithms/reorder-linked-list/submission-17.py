# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def print_list(self, head):
        c = head
        output = []
        while c:
            output.append(c.val)
            c = c.next
        return output

    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

    def mergeLists(self, l1, l2):
        dummyRes = c =  ListNode()
        # print()
        while l1 and l2:
            # print(self.print_list(l1), self.print_list(l2))
            c.next = l1
            l1 = l1.next

            c.next.next = l2 
            l2 = l2.next

            c = c.next.next

        c.next = l2
        return dummyRes.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        c, length = head, 0
        while c:
            length += 1
            c = c.next

        h1 = h2 = head
        for _ in range(length // 2 - 1):
            h2 = h2.next

        tmp = h2.next
        h2.next = None
        h2 = tmp
        
        print(self.print_list(h1), self.print_list(h2), self.print_list(head))
        h2 = self.reverseList(h2)
        print(self.print_list(h1), self.print_list(h2), self.print_list(head))

        c1, c2 = h1, h2
        while h1 and h2:
            tmp1 = h1.next
            h1.next = h2
            h1 = tmp1

            tmp2 = h2.next
            h2.next = h1 if h1 else tmp2
            h2 = tmp2





















