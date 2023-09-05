# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for i in range(left-1):
            prev = prev.next

        curr = prev.next
        nxt = curr.next

        for i in range(right - left):
            temp = nxt.next
            nxt.next = curr
            curr = nxt
            nxt = temp
        
        prev.next.next = nxt
        prev.next = curr
        return dummy.next
