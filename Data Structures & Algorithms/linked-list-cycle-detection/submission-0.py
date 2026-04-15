# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i = 0
        c = head
        my_dict = {}
        while c:
            if c not in my_dict:
                my_dict[c] = i
            else:
                return True
            i += 1
            c = c.next
        return False


# time: O(n)
# space: O(n)
