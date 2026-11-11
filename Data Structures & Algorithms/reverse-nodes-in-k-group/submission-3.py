# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

# time: O(k)
# space: O(1)

    def reverseList(self, groupCurr, groupNext):
        prev, curr = groupNext, groupCurr

        while curr != groupNext:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

# time: O(k) with k length of linked list 
# space: O(1)

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = groupPrev = ListNode(0, head)

        while True:
            kth = self.getKthNode(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next
            groupCurr = groupPrev.next
            
            groupPrev.next = self.reverseList(groupCurr, groupNext)
            groupPrev = groupCurr

        return dummy.next

# time: O(k) for getting kth node + O(k) for reversing, and that is done how many times: O(n / k) groups, so total complexity is: O(n) with n length of linked list given
# space: O(1)

            

            
            


    