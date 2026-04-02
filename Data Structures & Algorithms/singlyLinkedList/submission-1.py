class ListNode:
    def __init__(self, val, next_n=None):
        self.val = val
        self.next = next_n

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def get(self, index: int) -> int:
        if not self.IndexValid(index):
            return -1

        curr = self.head
        count = 0

        while curr:
            if count == index:
                return curr.val
            count += 1
            curr = curr.next

    def insertHead(self, val: int) -> None:
        head_node = self.createNode(val, self.head)
        self.head = head_node

        if self.length == 0:
            self.tail = self.head

        self.length += 1

    def insertTail(self, val: int) -> None:
        tail_node = self.createNode(val)
        if self.length > 0:
            self.tail.next = tail_node
        else:
            self.head = tail_node

        self.tail = tail_node

        self.length += 1
        
    def remove(self, index: int) -> bool:
        if not self.IndexValid(index):
            return False

        prev = None
        curr = self.head
        count = 0

        while curr:
            if count == index:
                if index == 0:
                    self.head = self.head.next
                elif index == self.length - 1:
                    prev.next = None
                    self.tail = prev
                else:
                    prev.next = curr.next

                self.length -= 1
                return True

            count += 1
            prev = curr
            curr = curr.next

    def getValues(self) -> List[int]:
        res = []
        curr = self.head

        while curr:
            res.append(curr.val)
            curr = curr.next

        return res


    def createNode(self, val: int, nextn=None) -> ListNode:
        return ListNode(val, nextn)

    def IndexValid(self, index):
        if index >= self.length:
            return False

        return True
        

        
