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

    def reverseList(self, groupCurr, groupPrev, groupNext):
        prev, curr = groupNext, groupCurr

        while curr != groupNext:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = groupPrev = ListNode(0, head)

        while True:
            kth = self.getKthNode(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next
            groupCurr = groupPrev.next
            
            groupPrev.next = self.reverseList(groupCurr, groupPrev, groupNext)
            groupPrev = groupCurr

        return dummy.next


            

            
            


    