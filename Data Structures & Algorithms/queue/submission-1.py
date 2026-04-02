class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self) -> bool:
        return self.length == 0
        

    def append(self, value: int) -> None:
        node = ListNode(value, next=None, prev=self.tail)

        if not self.isEmpty():
            self.tail.next = node
        else:
            self.head = node

        self.tail = node
        self.length += 1

    def appendleft(self, value: int) -> None:
        node = ListNode(value, next=self.head, prev=None)

        if not self.isEmpty():
            self.head.prev = node
        else:
            self.tail = node

        self.head = node
        self.length += 1
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        right = self.tail.val
        self.tail = self.tail.prev
        self.length -= 1
        return right
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        left = self.head.val
        self.head = self.head.next
        self.length -= 1
        return left
        
