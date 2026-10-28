# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = cursor = ListNode()
        list1, list2 = list1, list2
        while list1 and list2:
            if list1.val <= list2.val:
                cursor.next = list1
                list1 = list1.next
            else:
                cursor.next = list2
                list2 = list2.next
            cursor = cursor.next
        cursor.next = list2 if not list1 else list1
        return head.next

# time: O(n + m)
# space: O(1) auxiliary space