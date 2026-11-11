# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self, l1, l2):
        dummyRes = c = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                c.next = l1
                l1 = l1.next
            else:
                c.next = l2
                l2 = l2.next
            c = c.next
        c.next = l1 if l1 else l2
        return dummyRes.next

# time: O(n + m) with n and m lengths of l1 and l2 respectively 
# space: O(1)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None

                mergedLists.append(self.mergeTwoLists(l1, l2))
            lists = mergedLists
        return lists[0]


# time: O(logk for the while loop * n for inside for loop work) = O(nlogk) with k number of lists and n total number of nodes
# space: O(k/2)=O(k) auxiliary space for mergedLists list








