# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        current = head
        less, greater = ListNode(0), ListNode(0)
        less_tail, greater_tail = less, greater

        while current:
            if current.val < x:
                less_tail.next = ListNode(current.val)
                less_tail = less_tail.next
            else:
                greater_tail.next = ListNode(current.val)
                greater_tail = greater_tail.next
            current = current.next

        less_tail.next = greater.next
        return less.next
