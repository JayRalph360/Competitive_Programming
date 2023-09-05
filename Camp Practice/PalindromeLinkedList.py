# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def check(head):
            if (head == None):
                return True
            res = check(head.next) and (self.temp.val == head.val)
            self.temp = self.temp.next
            return res

        self.temp = head
        return check(head)
