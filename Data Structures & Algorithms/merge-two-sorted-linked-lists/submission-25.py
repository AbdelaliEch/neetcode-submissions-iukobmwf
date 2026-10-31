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

    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = list1, list2
        dummy_head = c3 = ListNode()

        while c1 and c2:
            if c1.val < c2.val:
                c3.next = c1
                c1 = c1.next
            else:
                c3.next = c2
                c2 = c2.next
            c3 = c3.next
        
        c3.next = c1 if c1 else c2
        return dummy_head.next

# time: O(n + m)
# space: O(1) auxiliary space