class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyCircularDeque:

    def __init__(self, k: int):
        self.head = self.tail = None
        self.size = 0
        self.maxSize = k

    def insertFront(self, value: int) -> bool:
        if self.size == self.maxSize:
            return False
        if not self.size:
            self.head = self.tail = ListNode(value)
        else:
            node = ListNode(value, next=self.head)
            self.head.prev = node
            self.head = node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.maxSize:
            return False
        if not self.size:
            self.head = self.tail = ListNode(value)
        else:
            node = ListNode(value, prev=self.tail)
            self.tail.next = node
            self.tail = node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if not self.size:
            return False
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if not self.size:
            return False
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.head.val if self.size else -1

    def getRear(self) -> int:
        return self.tail.val if self.size else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.maxSize


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
