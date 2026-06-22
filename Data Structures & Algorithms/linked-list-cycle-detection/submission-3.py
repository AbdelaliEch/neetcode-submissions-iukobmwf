# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        c1 = head
        my_set = set()

        while c1:
            # print(my_set, c1.val)
            if c1 in my_set:
                return True
            my_set.add(c1)
            c1 = c1.next
        return False