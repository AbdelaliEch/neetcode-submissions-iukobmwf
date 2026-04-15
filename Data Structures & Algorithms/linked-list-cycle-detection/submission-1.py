# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_pointer, slow_pointer = head, head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if fast_pointer == slow_pointer:
                return True
        return False

# Floyd's cycle detection algorithm:
# Floyd's cycle detection: slow moves 1 step, fast moves 2 steps.
# If no cycle, fast reaches None.
# If cycle exists, once both pointers are inside the cycle,
# fast gains 1 step on slow per iteration.
# The gap shrinks by 1 each time until it reaches 0 → they meet.
        
# time: O(n)
# space: O(1)
