# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head1 = odd = ListNode()
        head2 = even = ListNode()
        curr = head
        i = 0
        while curr:
            if i % 2 == 0:
                even.next = curr
                even = even.next
            else:
                odd.next = curr
                odd = odd.next
            curr = curr.next
            i += 1
        odd.next = None
        even.next = head1.next

        return head2.next
